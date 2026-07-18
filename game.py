import pygame
from constant import *
from ball import Ball
from tube import Tube


class Game:

    def __init__(self):
        self.reset()

    def reset(self):
        self.selected = None
        self.held_ball = None
        self.held_x = 0
        self.held_y = 0
        self.source_tube = None
        self.moves = 0

        self.tubes = [
            Tube(START_X, TUBE_Y),
            Tube(START_X + GAP, TUBE_Y),
            Tube(START_X + GAP * 2, TUBE_Y),
            Tube(START_X + GAP * 3, TUBE_Y)
        ]

        self.tubes[0].balls = [
            Ball(RED), Ball(BLUE), Ball(GREEN), Ball(RED)
        ]

        self.tubes[1].balls = [
            Ball(BLUE), Ball(RED), Ball(BLUE), Ball(GREEN)
        ]

        self.tubes[2].balls = [
            Ball(GREEN), Ball(RED)
        ]

        self.tubes[3].balls = []

    def pick(self, tube):

        if self.held_ball is not None:
            return

        if tube < 0 or tube >= len(self.tubes):
            return

        if self.tubes[tube].is_empty():
            return

        self.source_tube = tube
        self.held_ball = self.tubes[tube].remove_ball()
        self.selected = self.held_ball

    def drop(self, tube):

        if self.held_ball is None:
            return

        if tube < 0 or tube >= len(self.tubes):
            self.tubes[self.source_tube].add_ball(self.held_ball)

        elif self.tubes[tube].can_accept(self.held_ball):
            self.tubes[tube].add_ball(self.held_ball)
            self.moves += 1

        else:
            self.tubes[self.source_tube].add_ball(self.held_ball)

        self.held_ball = None
        self.selected = None
        self.source_tube = None

    def draw(self, screen):

        for tube in self.tubes:
            tube.draw(screen)

        if self.held_ball is not None:
            self.held_ball.x = self.held_x
            self.held_ball.y = self.held_y
            self.held_ball.draw(screen)