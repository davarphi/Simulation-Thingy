import pygame
import sys

pygame.init()

WINDOW = pygame.display.set_mode((576, 672))
pygame.display.set_caption("Pyhou")

CLOCK = pygame.time.Clock()
running = True

player_x = WINDOW.get_width()/2
player_y = WINDOW.get_height()/2
speed = 2
player_input = {"left":False, "right":False, "up":False, "down":False}
player_velocity = [0, 0]

def check_input(key, value):
    if key == pygame.K_LEFT:
        player_input["left"] = value
    elif key == pygame.K_UP:
        player_input["up"] = value
    elif key == pygame.K_DOWN:
        player_input["down"] = value
    elif key == pygame.K_RIGHT:
        player_input["right"] = value
    
while running:
    WINDOW.fill((128, 128, 128))

    CLOCK.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            check_input(event.key, True)
        elif event.type == pygame.KEYUP:
            check_input(event.key, False)

    player_velocity[0] = player_input["right"] - player_input["left"]
    player_velocity[1] = player_input["down"] - player_input["up"]


    pygame.draw.rect(WINDOW, (128, 0, 0), (player_x, player_y, 8, 8))

    player_x += player_velocity[0]*speed
    player_y += player_velocity[1]*speed

    pygame.display.update()

pygame.quit()