import pygame
from pygame.math import Vector2

class Player:
    def __init__(self, pos_x, pos_y, bound):
        self.BASE_SPEED = 3

        self.pos = Vector2(pos_x, pos_y)
        self.vel = Vector2(0,0)
        #self.w = 8
        #self.h = 8
        self.r = 6
        self.bound = bound

    def update_pos(self, player_input):
        self.vel.x = player_input["right"] - player_input["left"]
        self.vel.y = player_input["down"] - player_input["up"]

        speed = self.BASE_SPEED if not(player_input["slow"]) else self.BASE_SPEED/2

        if self.vel !=Vector2(0,0):
            self.pos += Vector2.normalize(self.vel)*speed

        bound_w = self.bound[0]
        bound_h = self.bound[1]
        if (self.pos.x < self.r): 
            self.pos.x = self.r
        elif (self.pos.x > bound_w - self.r): 
            self.pos.x = bound_w - self.r

        if (self.pos.y < self.r): 
            self.pos.y = self.r
        elif (self.pos.y > bound_h - self.r): 
            self.pos.y = bound_h - self.r
        #TODO: movement on window boujnd
    
    def display(self, window):
        pygame.draw.circle(window, (128, 0, 0), (self.pos.x, self.pos.y), self.r)






