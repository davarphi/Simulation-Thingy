import pygame
from pygame.math import Vector2

class Enemy:
    def __init__(self, pos_x, pos_y):
        self.pos = Vector2(pos_x, pos_y)

        #self.w = 16
        #self.h = 32

        self.r = 14

        self.health = 100.0

    def draw(self, window):
        pygame.draw.circle(window, (0, 128, 128), (self.pos.x, self.pos.y), self.r)
        pygame.draw.circle(window, (0, 0, 0), (self.pos.x, self.pos.y), self.r, 1) 
     
            


    








