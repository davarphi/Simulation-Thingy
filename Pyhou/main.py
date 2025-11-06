import pygame
import pygame.math as PG 
from components.player import Player
from components.projectile import Projectile

pygame.init()

WINDOW = pygame.display.set_mode((576, 672))
pygame.display.set_caption("Pyhou")

CLOCK = pygame.time.Clock()
running = True

Player.set_bound(WINDOW)
Projectile.set_bound(WINDOW)
player = Player(WINDOW.get_width()/2, WINDOW.get_height()/2)
player_input = {"left":False, "right":False, "up":False, "down":False, "slow":False, "shoot":False}

def check_input(key, value):
    if key == pygame.K_LEFT:
        player_input["left"] = value
    elif key == pygame.K_UP:
        player_input["up"] = value
    elif key == pygame.K_DOWN:
        player_input["down"] = value
    elif key == pygame.K_RIGHT:
        player_input["right"] = value
    elif key == pygame.K_LSHIFT:
        player_input["slow"] = value
    elif key == pygame.K_z:
        player_input["shoot"] = value
    
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
            
    player.draw(WINDOW)
    pygame.display.update()

pygame.quit()