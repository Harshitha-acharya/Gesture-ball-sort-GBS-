import pygame
from constant import *

class Tube:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.balls = []

    def push(self, ball):

        if len(self.balls) < MAX_BALLS:
            self.balls.append(ball)

    def pop(self):

        if len(self.balls) == 0:
            return None

        return self.balls.pop()

    def top(self):

        if len(self.balls) == 0:
            return None

        return self.balls[-1]

    def empty(self):

        return len(self.balls) == 0

    def full(self):

        return len(self.balls) == MAX_BALLS

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            BLACK,
            (self.x, self.y, TUBE_WIDTH, TUBE_HEIGHT),
            3
        )

        for i, ball in enumerate(reversed(self.balls)):

            ball.draw(
                screen,
                self.x + TUBE_WIDTH // 2,
                self.y + TUBE_HEIGHT - 30 - i * 55
            )