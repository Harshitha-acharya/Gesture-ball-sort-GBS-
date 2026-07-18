# ball.py

import pygame
from constant import BALL_RADIUS

class Ball:
    def __init__(self, color):
        self.color = color
        self.x = 0
        self.y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), BALL_RADIUS)