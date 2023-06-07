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

GRAVITY = 0.5  # Acceleration due to gravity

frame_counter = 0

screen_height = 0
screen_width = 0

bg = None
bg_x = 0

character_x = 0
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


def setup_game(pygame_load, screen_load):
    global pygame, screen, screen_height, screen_width, running, bg, track, sand_area_51, sand_area_51_x, dr_magnus_blackthorn_1, clock, bg_x, frame_counter, img_to_load, jumping, overstep_line_x

    pygame = pygame_load
    screen = screen_load
    clock = pygame.time.Clock()
    bg_x = 0
    frame_counter = 0

    pygame.display.set_caption("Pixler Jump")

    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h

    running = True

    setup_background_images()
    img_to_load = setup_characters(pygame)

    sand_area_51_x = screen_width * 1.75

    screen.fill((255, 0, 255))

    pygame.display.flip()
    game_start()


def game_start():
    global bg_x, character_x, character_y, character_velocity_y, GRAVITY, jumping, calculated, bar_speed, landed, bg
    global rect_bar_x, running, sand_area_51
    character_y = (screen_height - screen_height // 5) - 150
    direction = 1
    bar_speed = 30
    ended = False
    while running:
        if not ended:
            event_handler()
            paint_screen()

        if jumping:
            paint_bar()
            rect_bar_x += direction * bar_speed
            if rect_bar_x <= 0 or rect_bar_x >= screen_width - 50:
                direction *= -1.05

        if calculated and not landed:
            character_y += character_velocity_y
            character_velocity_y += GRAVITY

        if jumping and character_y > (screen_height - screen_height // 5) - 150:
            jumping = False
            landed = True
            ended = True
            jump_result = "You jumped " + str(clamp(character_x - sand_area_51_x, 0, 9999)) + "m"
            title_text = pygame.font.Font(None, 48).render(jump_result, True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 3))

            screen.blit(title_text, title_rect)
        pygame.display.update()
        if character_x + 185 > sand_area_51_x and not jumped:
            ended = True
            title_text = pygame.font.Font(None, 48).render("Overstepped", True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 3))

            screen.blit(title_text, title_rect)

        clock.tick(60)


def paint_screen():
    global frame_counter, img_to_load, character_y, character_x
    paint_base()
    frame_counter += 1
    if frame_counter % 10 == 0 and character_running:
        img_to_load = get_character()
    screen.blit(img_to_load, (character_x, character_y))
    if (bg_x <= -screen_width * 1.5 and (character_running or calculated) and not landed) or \
            (character_x < screen_width - 200 and calculated and not landed):
        character_x += 10


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
    global running
    for event in pygame.event.get():
        keyboard_event_handler(event)
        mouse_click_event_handler(event)


def mouse_click_event_handler(event):
    global running
    if event.type == pygame.QUIT:
        running = False


def keyboard_event_handler(event):
    global jumping, character_velocity_y, jump_force, jumped, character_running, bar_speed, calculated, screen_width
    global jump_point, landed
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            if not jumped:
                character_running = True
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
    bg = pygame.image.load("../img/infGameBackground.jpg").convert()
    bg = pygame.transform.scale(bg, (screen_width * 2.5, screen_height - screen_height // 5))

    track = pygame.image.load("../img/runningTrack.png").convert()
    track = pygame.transform.scale(track, (screen_width * 2, screen_height - screen_height // 5))

    sand_area_51 = pygame.image.load("../img/landingarea51.png").convert()
    sand_area_51 = pygame.transform.scale(sand_area_51, (screen_width * 0.75, screen_height - screen_height // 5))
