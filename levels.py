# levels.py

from ball import Ball
from constant import *

class Levels:

    def __init__(self):

        self.levels = [

            # Level 1
            [
                [RED, BLUE, GREEN, RED],
                [BLUE, RED, GREEN, BLUE],
                [GREEN, RED],
                []
            ],

            # Level 2
            [
                [RED, BLUE, GREEN, YELLOW],
                [GREEN, YELLOW, RED, BLUE],
                [BLUE, RED, YELLOW, GREEN],
                [],
                []
            ],

            # Level 3
            [
                [RED, BLUE, GREEN, PURPLE],
                [PURPLE, GREEN, RED, BLUE],
                [GREEN, RED, PURPLE, BLUE],
                [BLUE, PURPLE, RED, GREEN],
                [],
                []
            ]

        ]

    def load_level(self, level_number):

        if level_number >= len(self.levels):
            level_number = 0

        data = self.levels[level_number]

        tubes = []

        for tube in data:

            temp = []

            for color in tube:

                temp.append(Ball(color))

            tubes.append(temp)

        return tubes