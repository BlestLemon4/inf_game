import pygame
import sys
import game
from pygame.locals import *



# Initialize Pygame
pygame.init()
pygame.display.init()

# Set the dimensions of the screen
screen_width = 1680
screen_height = 1050
screen = pygame.display.set_mode((screen_width, screen_height))  # Initialize fullscreen display

pygame.display.set_caption("Pygame Menu")

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Set fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 48)

# Set menu items
menu_items = ["Start Game", "Options", "Quit"]
selected_item = None

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                for i, item in enumerate(menu_items):
                    item_text = font.render(item, True, GRAY)
                    item_rect = item_text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
                    if item_rect.collidepoint(pos):
                        if i == 0:
                            running = False
                            pygame.display.quit()
                            game.start_game()
                            # Add your game code here
                        elif i == 1:
                            print("Options selected")
                            # Add your options code here
                        elif i == 2:
                            running = False
                        break
    # Clear the screen
    screen.fill(BLACK)

    # Render the title
    title_text = title_font.render("Pygame Menu", True, WHITE)
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))
    screen.blit(title_text, title_rect)

    # Render the menu items
    for i, item in enumerate(menu_items):
        if i == selected_item:
            item_text = font.render(item, True, WHITE)
        else:
            item_text = font.render(item, True, GRAY)
        item_rect = item_text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
        screen.blit(item_text, item_rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
