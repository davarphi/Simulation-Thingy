import pygame
from pygame.math import Vector2

class Projectile:
    bound_w = None
    bound_h = None

    @classmethod
    def set_bound(cls, window):
        cls.bound_w = window.get_width()
        cls.bound_h = window.get_height()

    def __init__(self, pos_x, pos_y):
        start = Vector2(pos_x, pos_x)
        pos = Vector2(pos_x, pos_y)

        speed = 10
        r = 5
        vel = Vector2(0, 0)
        in_motion = False

        
        