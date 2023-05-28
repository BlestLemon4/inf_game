import sys
import game
from pygame.locals import *

menu_items = ["Start Game", "Options", "Quit"]
selected_item = None

running = True

pygame = None
screen = None
screen_width = None
screen_height = None

font = None
title_font = None

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

def menu_setup(screen_load, pygame_load):
    global pygame, screen, screen_height, screen_width, title_font, font
    pygame = pygame_load
    screen = screen_load
    pygame.display.set_caption("Pygame Menu")
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 48)
    run()

def run():
    global running
    while running:
        event_Handler()
        
        screen.fill(BLACK)

        title_text = title_font.render("Pygame Menu", True, WHITE)
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))
        screen.blit(title_text, title_rect)

        paint_menu()

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def paint_menu():
    # global GRAY, font
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
                item_text = font.render(item, True, GRAY)
                item_rect = item_text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
                if item_rect.collidepoint(pos):
                    if i == 0:
                        game.setup_game(pygame, screen)
                    elif i == 1:
                        print("Options selected")
                    elif i == 2:
                        running = False
                    break

def keyboard_event_handler(event):
    pass
