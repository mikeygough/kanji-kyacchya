# Kanji
from GameObject import GameObject
from constants import LANES
from random import randint, choice


class Kanji(GameObject):
    def __init__(self, image):
        super().__init__(0, 0, image)
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = choice(LANES)
        self.y = -64
