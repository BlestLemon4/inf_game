from pygame.locals import *
from pygame.math import lerp, clamp

from character_service import *

pygame = None
screen = None
clock = None

running = True
jumping = False
jumped = False
landed = False
character_running = False

frame_counter = 0

screen_height = 0
screen_width = 0

bg = None
bg_x = 0

character_x = 0.0
character_y = 0
character_velocity_y = 0
jump_force = 0  # Initial upward velocity for the jump

calculated = False
rect_bar_x = 0
bar_speed = 0

track = None
sand_area_51 = None
sand_area_51_x = 0

img_to_load = None

end_attempt_event = None
end_attempt = False

menu_items = ["Restart", "Back"]
font = None


def setup_game(pygame_load, screen_load):
    global pygame, screen, font, end_attempt_event

    pygame = pygame_load
    screen = screen_load

    music_path = "../resources/music/background_play.mp3"
    pygame.mixer.music.load(music_path)

    font = pygame.font.Font(None, 36)
    end_attempt_event = pygame.USEREVENT + 2
    pygame.display.set_caption("Pixler Jump")
    reset_game_state()

    pygame.display.flip()
    game_start()


def reset_game_state():
    global clock, frame_counter, screen_height, screen_width, running, img_to_load, sand_area_51_x, screen, bg_x
    global jumping, jumped, landed, character_running, bg, character_x, character_y, character_velocity_y, jump_force
    global calculated, rect_bar_x, bar_speed, track, end_attempt, end_attempt_event, pygame

    clock = pygame.time.Clock()
    bg_x = 0

    frame_counter = 0

    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h

    running = True
    jumping = False
    jumped = False
    landed = False
    character_running = False

    setup_background_images()
    img_to_load = setup_characters(pygame)

    sand_area_51_x = screen_width * 1.75

    screen.fill((255, 0, 255))

    frame_counter = 0

    bg_x = 0

    character_x = 0.0
    character_y = 0
    character_velocity_y = 0
    jump_force = 0  # Initial upward velocity for the jump

    calculated = False
    rect_bar_x = 0
    bar_speed = 0

    end_attempt = False


def game_start():
    global bg_x, character_x, character_y, character_velocity_y, jumping, calculated, bar_speed, landed, bg
    global rect_bar_x, running, sand_area_51, screen
    character_y = (screen_height - screen_height // 5) - 150
    direction = 1
    bar_speed = 30
    ended = False
    overstepped = False
    while running:
        if not ended:
            paint_screen()
        event_handler()

        if jumping and not overstepped:
            paint_bar()
            rect_bar_x += direction * bar_speed
            if rect_bar_x <= 0 or rect_bar_x >= screen_width - 50:
                if abs(direction) < 3:
                    direction *= -1.05
                else:
                    direction *= -1

        if calculated and not landed:
            character_y += character_velocity_y
            character_velocity_y += 0.5
        if character_x + 186 > sand_area_51_x and (not jumped or overstepped):
            overstepped = True
            show_overstep()

            if not ended:
                pygame.time.set_timer(pygame.USEREVENT + 2, 1500, loops=1)
                music_path = "../resources/music/drums.mp3"
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play()

            ended = True
        elif (jumping or ended) and character_y > (screen_height - screen_height // 5) - 150:
            show_score()
            if not ended:
                pygame.time.set_timer(pygame.USEREVENT + 2, 1500, loops=1)
                music_path = "../resources/music/drums.mp3"
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play()
                pygame.mixer.music.set_pos(4.4)
            ended = True

        pygame.display.update()
        if end_attempt:
            jumping = False
            screen.fill((0, 0, 0))
            show_options()
        clock.tick(60)


def show_score():
    global jumping, landed, screen, end_attempt, pygame
    jumping = False
    landed = True

    if not end_attempt:
        jump_result = ["You jumped..."]
        title_text = pygame.font.Font(None, 48).render(jump_result[0], True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 3))
        screen.blit(title_text, title_rect)
        return
    if int(clamp(character_x - sand_area_51_x, 0, 9999)) == 0:
        jump_result = ["...0cm??? HOW???",
                       "Bro..., do you know what the so called 'Long jump' is?",
                       "Like how it works and that you have to jump as far as possible?",
                       "And like not on the track... 'cause the jump length is measured from the beginning of the "
                       "sandarea 51?",
                       "Yes? Okay now try again... or just Alt + F4 and we'll never see each other again!"]
    else:
        jump_result = ["..." + str(round(float(clamp(character_x - sand_area_51_x, 0, 9999)), 2)) + "cm"]

    y_pos = screen_height // 3
    for line in jump_result:
        title_text = pygame.font.Font(None, 48).render(line, True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen_width // 2, y_pos))
        screen.blit(title_text, title_rect)
        y_pos += 50


def show_overstep():
    global screen
    title_text = pygame.font.Font(None, 48).render("Overstepped", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 3))

    screen.blit(title_text, title_rect)


def show_options():
    global menu_items, font
    pos = pygame.mouse.get_pos()

    for i, item in enumerate(menu_items):
        item_text = font.render(item, True, (255, 255, 255))
        item_rect = item_text.get_rect(center=(screen_width // 2, screen_height // 2 + (i + 2) * 50))

        if item_rect.collidepoint(pos):
            item_text = font.render(item, True, (100, 100, 100))

        screen.blit(item_text, item_rect)


def paint_screen():
    global frame_counter, img_to_load, character_y, character_x
    paint_base()
    frame_counter += 1
    if frame_counter % 10 == 0 and character_running:
        img_to_load = get_character_frame()
    screen.blit(img_to_load, (character_x, character_y))
    if (bg_x <= -screen_width * 1.5 and (character_running or calculated) and not landed) or \
            (character_x < screen_width - 200 and calculated and not landed):
        character_x += screen_width / 170


def paint_base():
    global bg_x, sand_area_51_x, bg, track, sand_area_51, sand_area_51_x

    screen.blit(bg, (bg_x, 0))
    screen.blit(track, (bg_x, screen_height - screen_height // 5))

    if bg_x * -2.5 > sand_area_51_x:
        screen.blit(sand_area_51, (sand_area_51_x, screen_height - screen_height // 5))
    if bg_x + screen_width * 2.5 > screen_width and character_running:
        bg_x -= 10
        sand_area_51_x -= 10


def paint_bar():
    global screen_width
    rect_x = 0
    rect_y = 200
    rect_width = screen_width
    rect_heigth = 50
    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_width, rect_heigth))
    pygame.draw.rect(screen, (255, 128, 0), (rect_x + screen_width / 4, rect_y, rect_width / 2, rect_heigth))
    pygame.draw.rect(screen, (0, 255, 0),
                     (rect_x + screen_width / 2 - rect_width / 16, rect_y, rect_width / 8, rect_heigth))
    pygame.draw.rect(screen, (0, 0, 0), (rect_bar_x, rect_y, 50, rect_heigth))


def event_handler():
    global running, end_attempt_event, end_attempt
    for event in pygame.event.get():
        if event.type == end_attempt_event:
            end_attempt = True
        keyboard_event_handler(event)
        mouse_click_event_handler(event)


def mouse_click_event_handler(event):
    global running
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            pos = pygame.mouse.get_pos()
            for i, item in enumerate(menu_items):
                item_text = font.render(item, True, (100, 100, 100))
                item_rect = item_text.get_rect(center=(screen_width // 2, screen_height // 2 + (i + 2) * 50))
                if item_rect.collidepoint(pos):
                    if i == 0:
                        setup_game(pygame, screen)
                    elif i == 1:
                        running = False
                    break


def keyboard_event_handler(event):
    global jumping, character_velocity_y, jump_force, jumped, character_running, bar_speed, calculated, screen_width
    global jump_point, landed, pygame
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            if not jumped:
                character_running = True
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_pos(2)
    if event.type == KEYUP:
        if event.key == K_SPACE:
            if jumped and not calculated:
                bar_speed = 0
                difference = abs((rect_bar_x + 25) / (screen_width / 2) - 1)
                if difference == 0:
                    difference = 0.01

                jump_force = lerp(0, 1, 1 - difference) * -110

                character_velocity_y = jump_force / 5
                calculated = True
            if not jumped:
                jumping = True
                jumped = True
                character_running = False


def setup_background_images():
    global bg, track, sand_area_51
    bg = pygame.image.load("../resources/play_background/infGameBackground.jpg").convert()
    bg = pygame.transform.scale(bg, (screen_width * 2.5, screen_height - screen_height // 5))

    track = pygame.image.load("../resources/play_background/runningTrack.png").convert()
    track = pygame.transform.scale(track, (screen_width * 2, screen_height - screen_height // 5))

    sand_area_51 = pygame.image.load("../resources/play_background/landingarea51.png").convert()
    sand_area_51 = pygame.transform.scale(sand_area_51, (screen_width * 0.75, screen_height - screen_height // 5))
