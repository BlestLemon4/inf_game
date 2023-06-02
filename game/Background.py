import pygame
import pygame_menu

pygame.init()
screen = pygame.display.set_mode((800, 600))  # Set the screen dimensions

theme = pygame_menu.themes.THEME_DEFAULT  # Choose a theme (you can also create your own)
theme.background_color = (0, 0, 0)  # Set the background color
theme.widget_background_color = (0, 0, 0)  # Set the widget background color
theme.background_image = pygame_menu.baseimage.BaseImage("C:\Users\Startklar\PycharmProjects\inf_game\img\2a172f4a-f978-422c-a817-38d66c6c8bf1.jpg")


