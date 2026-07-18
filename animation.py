# animation.py

import pygame

class BallAnimation:

    def __init__(self):
        self.active = False
        self.ball = None

        self.start_x = 0
        self.start_y = 0

        self.end_x = 0
        self.end_y = 0

        self.current_x = 0
        self.current_y = 0

        self.speed = 12

    def start(self, ball, sx, sy, ex, ey):

        self.ball = ball

        self.start_x = sx
        self.start_y = sy

        self.end_x = ex
        self.end_y = ey

        self.current_x = sx
        self.current_y = sy

        self.active = True

    def update(self):

        if not self.active:
            return

        dx = self.end_x - self.current_x
        dy = self.end_y - self.current_y

        distance = (dx**2 + dy**2) ** 0.5

        if distance < self.speed:

            self.current_x = self.end_x
            self.current_y = self.end_y

            self.active = False
            return

        self.current_x += self.speed * dx / distance
        self.current_y += self.speed * dy / distance

    def draw(self, screen):

        if not self.active:
            return

        pygame.draw.circle(
            screen,
            self.ball.color,
            (int(self.current_x), int(self.current_y)),
            25
        )

        pygame.draw.circle(
            screen,
            (0,0,0),
            (int(self.current_x), int(self.current_y)),
            25,
            2
        )

    def is_running(self):
        return self.active