from pygame.locals import *
from character_service import *

pygame = None
screen = None
clock = None

running = True

frame_counter = 0

screen_height = None
screen_width = None

bg  = None
bg_x = 0
track = None
sand_area_51 = None
sand_area_51_x = None

img_to_load = None

def setup_game(pygame_load, screen_load):
    global pygame, screen, screen_height, screen_width, running, bg, track, sand_area_51, sand_area_51_x, dr_magnus_blackthorn_1, clock, bg_x, frame_counter, img_to_load

    pygame = pygame_load
    screen = screen_load
    clock = pygame.time.Clock()
    bg_x = 0
    frame_counter = 0
    
    pygame.display.set_caption("Pygame Menu")
    
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h

    running = True

    setup_images()
    img_to_load = setup_characters(pygame)
    print("After Load")
    print(img_to_load)
    
    sand_area_51_x = screen_width * 1.75
    
    screen.fill((255, 0, 255))
    
    pygame.display.flip()
    game_start()

def game_start():
    global bg_x
    while running:
        event_Handler()
        paint_screen()
        
        pygame.display.update()
        clock.tick(60)

def paint_screen():
    global frame_counter, img_to_load
    paint_base()
    frame_counter += 1
    if frame_counter % 10 == 0:
        img_to_load = get_character()
    screen.blit(img_to_load, (100, (screen_height - screen_height // 5) - 150))

def paint_base():
    global bg_x, sand_area_51_x, bg, track, sand_area_51, sand_area_51_x

    screen.blit(bg, (bg_x, 0))
    screen.blit(track, (bg_x, screen_height - screen_height // 5))

    if bg_x * -2.5 > sand_area_51_x:
        screen.blit(sand_area_51, (sand_area_51_x, screen_height - screen_height // 5))
    if bg_x + screen_width * 2.5 > screen_width:
        bg_x -= 10
        sand_area_51_x -= 10

def event_Handler():
    global running
    for event in pygame.event.get():
            keyboard_event_handler(event)
            mouse_click_event_handler(event)


def mouse_click_event_handler(event):
    global running
    if event.type == pygame.QUIT:
        running = False

def keyboard_event_handler(event):
    global running
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            running = False

def setup_images():
    global bg, track, sand_area_51
    bg = pygame.image.load("img/infGameBackground.jpg").convert()
    bg = pygame.transform.scale(bg, (screen_width * 2.5, screen_height - screen_height // 5))

    track = pygame.image.load("img/runningTrack.png").convert()
    track = pygame.transform.scale(track, (screen_width * 2, screen_height - screen_height // 5))

    sand_area_51 = pygame.image.load("img/landingarea51.png").convert()
    sand_area_51 = pygame.transform.scale(sand_area_51, (screen_width * 0.75, screen_height - screen_height // 5))
