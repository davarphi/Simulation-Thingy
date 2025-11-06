import pygame
from pygame.math import Vector2
from math import sin, cos, pi

class Projectile:
    bound_w = None
    bound_h = None

    @classmethod
    def set_bound(cls, window):
        cls.bound_w = window.get_width()
        cls.bound_h = window.get_height()

    def __init__(self, pos_x, pos_y, angle_off):
        start = Vector2(pos_x, pos_x)
        pos = Vector2(pos_x, pos_y)
        speed = 10
        vel = Vector2(cos(pi/2 + angle_off), sin(pi/2 + angle_off))*speed
        r = 5

    def update(self):
        self.pos += self.vel
    
    def draw(self, window):
        pygame.draw.circle(window, (128, 0, 0, 50), (self.pos.x, self.pos.y), self.r)
        pygame.draw.circle(window, (0, 0, 0, 50), (self.pos.x, self.pos.y), self.r, 1)

    # def fire(self, new_pos_x, new_pos_y, player_input, flag):
    #     if (player_input["slow"]):
    #         self.attack_deg = radians(2)
    #     elif (not player_input["slow"]):
    #         self.attack_deg = radians(4)

    #     self.pos = Vector2(new_pos_x, new_pos_y)

    #     if (self.in_motion):
    #         match flag:
    #             case 0:
    #                 self.vel = Vector2(cos(pi/2 + self.attack_deg), -sin(pi/2 + self.attack_deg))*self.speed
    #             case 1:
    #                 self.vel = Vector2(0, -self.speed)
    #             case 2:
    #                 self.vel = Vector2(cos(pi/2 - self.attack_deg), -sin(pi/2 + self.attack_deg))*self.speed
            
    #         self.pos += self.vel
    #         self.in_motion = True
    

    def is_out_bound(self):
        return self.pos.y < self.r/2 or self.pos.y > self.bound_h - self.r/2
    



        
        