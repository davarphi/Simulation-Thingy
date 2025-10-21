import pygame
from pygame.math import Vector2

class Player:
    def __init__(self, pos_x, pos_y):
        self.BASE_SPEED = 3

        self.pos = Vector2(pos_x, pos_y)
        self.vel = Vector2(0,0)
        self.w = 8
        self.h = 8

    def update_pos(self, player_input):
        self.vel.x = player_input["right"] - player_input["left"]
        self.vel.y = player_input["down"] - player_input["up"]

        speed = self.BASE_SPEED if not(player_input["slow"]) else self.BASE_SPEED/2

        if self.vel !=Vector2(0,0):
            self.pos += Vector2.normalize(self.vel)*speed
    
    def display(self, window):
        pygame.draw.rect(window, (128, 0, 0), (self.pos.x, self.pos.y, 8, 8))






