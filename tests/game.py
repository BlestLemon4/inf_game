import pygame
from pygame.locals import *

# Bildschirmgröße
pygame.init()
pygame.display.init()

display_info = pygame.display.Info()
screen_width = 1680
screen_height = 1050
# Position und Größe des Bodens
ground_y = screen_height * 5 // 6  # Verschiebung um die Hälfte nach unten
ground_height = screen_height // 6  # Größe um die Hälfte reduziert

# Position und Größe des Balls
ball_radius = 20
ball_x = screen_width // 14  # Startposition im linken Viertel des Bildschirms
ball_y = ground_y - ball_radius

# Geschwindigkeit und Beschleunigung des Balls
ball_speed = 5
ball_jump_power = -20
ball_gravity = 1

# Position und Größe des Sandbereichs
sand_x = screen_width // 1.125
sand_y = ground_y
sand_width = screen_width // 3
sand_height = ground_height

# Position und Größe des weinroten Bereichs
wine_red_x = screen_width // 1.125 - sand_width * 2 // 3  # Ein Drittel der Breite des gelben Bereichs
wine_red_y = ground_y
wine_red_width = sand_width // 3  # Ein Drittel der Breite des gelben Bereichs
wine_red_height = ground_height

# Status des Ball-Sprungs
ball_jump = False
ball_jump_velocity = 0
can_jump = True
jumping = False
jumpStrength = 0

rect_x = 0;
rect_y = 200
rect_bar_x = 0
bar_speed = 30
direction = 1

# Funktion für die Bewegung des Balls nach rechts
def move_right():
    ball_x += ball_speed


def start_game():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))  # Initialize fullscreen display
    clock = pygame.time.Clock()

    global ball_x, ball_jump, ball_gravity, ball_radius, ball_jump_power, ball_y, can_jump, jumping, rect_x, rect_y, jumpStrength, rect_bar_x, bar_speed, direction, ball_speed

    # Initialisierung
    # Hauptprogrammschleife
    running = True
    calculated = False
    while running:
        screen.fill((255, 255, 255))  # Hintergrundfarbe

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == KEYUP:
                if event.key == K_SPACE:
                    if can_jump:
                        ball_jump = True
                        ball_jump_velocity = ball_jump_power
                        can_jump = False
                        jumping = True

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if jumping:
                        bar_speed = 0
                        diffrence = abs(rect_bar_x / (sand_width/2) - 1)
                        ball_jump_velocity = 1/diffrence * -25
                        ball_speed = 1/diffrence *25
                        calculated = True


        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            if can_jump:  # Überprüfe, ob die Leertaste gedrückt wird
                move_right()
           
        if jumping:
            rect_bar_x += direction * bar_speed
            if rect_bar_x <= 0 or rect_bar_x >= screen_width - 50:
                direction *= -1
                
        # Ballbewegung
        if calculated:
            if ball_jump:
                ball_y += ball_jump_velocity
                ball_jump_velocity += ball_gravity
                move_right()
            else:
                if ball_y < ground_y - ball_radius:
                    ball_y += ball_gravity

            if ball_y >= ground_y - ball_radius:
                ball_y = ground_y - ball_radius
                ball_jump_velocity = 0

            if ball_jump and ball_y == ground_y - ball_radius:
                ball_jump = False
                jumping = True

        # Begrenze den Ball auf den Bildschirm
        if ball_x < ball_radius:
            ball_x = ball_radius
        elif ball_x > screen_width - ball_radius:
            ball_x = screen_width - ball_radius

        # Zeichne den Boden
        pygame.draw.rect(screen, (144, 0, 0), (0, ground_y, screen_width, ground_height))  # Weinrot
        pygame.draw.rect(screen, (0, 0, 0), (wine_red_x, wine_red_y, wine_red_width, wine_red_height))  # Hellgelb
        pygame.draw.rect(screen, (210, 183, 115), (sand_x - sand_width // 2, sand_y, sand_width, sand_height))
        if jumping:
            rect_width = screen_width
            rect_heigth = 50
            pygame.draw.rect(screen, (255, 0, 0), (rect_x,rect_y,rect_width,rect_heigth))
            pygame.draw.rect(screen, (255, 128, 0), (rect_x + screen_width / 4,rect_y,rect_width / 2,rect_heigth))
            pygame.draw.rect(screen, (0, 255, 0), (rect_x + screen_width / 2 - rect_width / 16,rect_y,rect_width / 8,rect_heigth))
            pygame.draw.rect(screen, (0, 0, 0), (rect_bar_x, rect_y,50,rect_heigth))



        # Zeichne den Ball
        pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)

        pygame.display.flip()
        clock.tick(60)

    # Beenden des Programms
    pygame.quit()