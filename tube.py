import pygame
from constant import *

class Tube:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.balls = []

        self.rect = pygame.Rect(
            x,
            y,
            TUBE_WIDTH,
            TUBE_HEIGHT
        )

    def draw(self, screen):
        # Draw tube
        pygame.draw.rect(
            screen,
            WHITE,
            self.rect,
            3,
            border_radius=8
        )

        # Draw balls
        for i, ball in enumerate(self.balls):
            ball.x = self.x + TUBE_WIDTH // 2
            ball.y = self.y + TUBE_HEIGHT - BALL_RADIUS - (i * BALL_GAP)
            ball.draw(screen)

    def add_ball(self, ball):
        if len(self.balls) < MAX_BALLS:
            self.balls.append(ball)
            return True
        return False

    def remove_ball(self):
        if self.balls:
            return self.balls.pop()
        return None

    def top_ball(self):
        if self.balls:
            return self.balls[-1]
        return None

    def is_empty(self):
        return len(self.balls) == 0

    def is_full(self):
        return len(self.balls) >= MAX_BALLS

    def can_accept(self, ball):
        if self.is_full():
            return False

        if self.is_empty():
            return True

        return self.top_ball().color == ball.color