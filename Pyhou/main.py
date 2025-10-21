import pygame
import pygame.math as PG 

pygame.init()

WINDOW = pygame.display.set_mode((576, 672))
pygame.display.set_caption("Pyhou")

CLOCK = pygame.time.Clock()
running = True

speed = 3
player_input = {"left":False, "right":False, "up":False, "down":False}
player_pos = PG.Vector2(WINDOW.get_width()/2, WINDOW.get_height()/2)
player_velocity_dir = PG.Vector2(0, 0)

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

    player_velocity_dir.x = player_input["right"] - player_input["left"]
    player_velocity_dir.y = player_input["down"] - player_input["up"]

    pygame.draw.rect(WINDOW, (128, 0, 0), (player_pos.x, player_pos.y, 8, 8))

    if player_velocity_dir != PG.Vector2(0,0):
        player_pos += PG.Vector2.normalize(player_velocity_dir)*speed

    pygame.display.update()

pygame.quit()