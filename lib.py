import pygame
from random import randint

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

class Colors():
    def __init__(self):
        self.black = pygame.Color(0, 0, 0, 255)
        self.white = pygame.Color(255, 255, 255, 255)

    def get_random(self) -> pygame.Color:
        c = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
        return c
    
global_offset = pygame.math.Vector2()

color = Colors()
delta_time = 0
frame_limit = 120
events = None