import pygame
from pygame.math import Vector2
from math import radians
from projectile import Projectile

class Player:
    bound_w = None
    bound_h = None

    @classmethod
    def set_bound(cls, window):
        cls.bound_w = window.get_width()
        cls.bound_h = window.get_height()
    
    def __init__(self, pos_x, pos_y):
        self.BASE_SPEED = 5

        self.pos = Vector2(pos_x, pos_y)
        self.vel = Vector2(0,0)
        #self.w = 8
        #self.h = 8
        self.r = 7
        self.bullets = []

    def update_pos(self, player_input):
        self.vel.x = player_input["right"] - player_input["left"]
        self.vel.y = player_input["down"] - player_input["up"]

        speed = self.BASE_SPEED if not(player_input["slow"]) else self.BASE_SPEED/2

        if self.vel !=Vector2(0,0):
            self.pos += Vector2.normalize(self.vel)*speed

        if (self.pos.x < self.r): 
            self.pos.x = self.r
        elif (self.pos.x > self.bound_w - self.r): 
            self.pos.x = self.bound_w - self.r

        if (self.pos.y < self.r): 
            self.pos.y = self.r
        elif (self.pos.y > self.bound_h - self.r): 
            self.pos.y = self.bound_h - self.r
        #TODO: movement on window boujnd
    
    def display(self, window):
        pygame.draw.circle(window, (128, 0, 0), (self.pos.x, self.pos.y), self.r)
        pygame.draw.circle(window, (0, 0, 0), (self.pos.x, self.pos.y), self.r, 1)
    
    def update_proj(self, bullets):
        pass

    def shoot(self, player_state):
        if (player_state["slow"]):
            attack_degs = [-radians(4), 0, radians(4)]
        else:
            attack_degs = [-radians(2), 0, radians(2)]

        for angle in attack_degs:
            bullet = Projectile 








