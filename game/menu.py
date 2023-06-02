import sys
import game
import pygame

menu_items = ["Start Game", "Options", "Background", "Quit"]
selected_item = None
background_list = []
background = None
current_bg = 0

running = True

pygame = None
screen = None
screen_width = None
screen_height = None

change_Background_event = None

font = None
title_font = None

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)


def menu_setup(screen_load, pygame_load):
    global pygame, screen, screen_height, screen_width, title_font, font, change_Background_event,background_list
    pygame = pygame_load
    change_Background_event = pygame.USEREVENT + 1
    screen = screen_load
    pygame.display.set_caption("Pygame Menu")
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 48)
    background_0 = pygame.image.load('..\img\Bild 1.jpg')
    background_1 = pygame.image.load("..\img\Bild 2.jpg")
    background_2 = pygame.image.load("..\img\Bild 3.jpg")
    background_3 = pygame.image.load("..\img\Bild 4.jpg")
    background_4 = pygame.image.load("..\img\Bild 5.jpg")
    background_5 = pygame.image.load("..\img\Bild 6.jpg")
    background_0 = pygame.transform.smoothscale(background_0, (screen_width, screen_height))
    background_1 = pygame.transform.smoothscale(background_1, (screen_width, screen_height))
    background_2 = pygame.transform.smoothscale(background_2, (screen_width, screen_height))
    background_3 = pygame.transform.smoothscale(background_3, (screen_width, screen_height))
    background_4 = pygame.transform.smoothscale(background_4, (screen_width, screen_height))
    background_5 = pygame.transform.smoothscale(background_5, (screen_width, screen_height))
    background_list = []
    background_list.append(background_0)
    background_list.append(background_1)
    background_list.append(background_2)
    background_list.append(background_3)
    background_list.append(background_4)
    background_list.append(background_5)


    pygame.time.set_timer(pygame.USEREVENT+1, 1000,loops=0)
    run()


def run():
    global running
    global background
    background = background_list[0]
    while running:
        event_Handler()


        screen.fill(BLACK)

        title_text = title_font.render("Pygame Menu", True, WHITE)
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))

        screen.blits(((background, (0, 0)), (title_text, title_rect)))

        paint_menu()

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def paint_menu():
    pos = pygame.mouse.get_pos()
    for i, item in enumerate(menu_items):
        item_text = font.render(item, True, GRAY)
        item_rect = item_text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))

        if item_rect.collidepoint(pos):
            item_text = font.render(item, True, WHITE)

        item_rect = item_text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
        screen.blit(item_text, item_rect)


def event_Handler():
    global running

    for event in pygame.event.get():
        background_change_event_handler(event)
        keyboard_event_handler(event)
        mouse_click_event_handler(event)

def background_change_event_handler(event):
    global change_Background_event
    global background
    global background_list
    global current_bg
    if event.type == change_Background_event:
        if current_bg > len(background_list):
            current_bg = 0
        background = background_list[current_bg]
        current_bg =+ 1


def mouse_click_event_handler(event):
    global running
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            pos = pygame.mouse.get_pos()
            for i, item in enumerate(menu_items):
                item_text = font.render(item, True, GRAY)
                item_rect = item_text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
                if item_rect.collidepoint(pos):
                    if i == 0:
                        game.setup_game(pygame, screen)
                    elif i == 1:
                        print("Options selected")
                    elif i == 2:
                        running = False
                    elif i == 3:
                        print("Background selected")  # Replace with your background functionality code
                    break


def keyboard_event_handler(event):
    pass
