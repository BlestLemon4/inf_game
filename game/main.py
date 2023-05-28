import menu
import pygame

pygame.init()
pygame.display.init()

screen_width = 1680
screen_height = 1050
screen = pygame.display.set_mode((screen_width, screen_height))  # Initialize fullscreen display

menu.menu_setup(screen, pygame)