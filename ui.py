# ui.py

import pygame
from constant import *

class UI:

    def __init__(self):
        pygame.font.init()

        self.title_font = pygame.font.SysFont("Arial", 42, bold=True)
        self.text_font = pygame.font.SysFont("Arial", 28)
        self.small_font = pygame.font.SysFont("Arial", 22)

    def draw_title(self, screen):

        title = self.title_font.render(
            "Gesture Controlled Ball Sort Puzzle",
            True,
            (30, 30, 30)
        )

        screen.blit(title, (170, 20))

    def draw_moves(self, screen, moves):

        text = self.text_font.render(
            f"Moves : {moves}",
            True,
            BLACK
        )

        screen.blit(text, (30, 90))

    def draw_level(self, screen, level):

        text = self.text_font.render(
            f"Level : {level}",
            True,
            BLACK
        )

        screen.blit(text, (30, 130))

    def draw_instruction(self, screen):

        text = self.small_font.render(
            "Pinch thumb and index finger to pick/drop the ball",
            True,
            (70, 70, 70)
        )

        screen.blit(text, (180, 650))

    def draw_restart_button(self, screen):

        pygame.draw.rect(
            screen,
            (50, 150, 255),
            (820, 25, 140, 45),
            border_radius=8
        )

        txt = self.small_font.render(
            "Restart (R)",
            True,
            WHITE
        )

        screen.blit(txt, (842, 37))

    def draw_win(self, screen):

        win = self.title_font.render(
            "🎉 YOU WIN! 🎉",
            True,
            (0, 170, 0)
        )

        screen.blit(win, (310, 150))
