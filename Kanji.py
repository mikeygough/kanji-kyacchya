# Kanji
from GameObject import GameObject
from constants import LANES
from random import randint, choice


class Kanji(GameObject):
  def __init__(self, image):
    super().__init__(0, 0, image)
    self.dx = 0
    self.dy = 0
    self.reset()
    self.image = image
    
  def setImage(self, value):
      self.image = value

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
      self.reset()

  def reset(self):
    direction = randint(1, 4)
    if direction == 1: # left
      self.x = -64
      self.y = choice(LANES)
      self.dx = (randint(0, 200) / 100) + 1
      self.dy = 0
    elif direction == 2: # right
      self.x = 500
      self.y = choice(LANES)
      self.dx = ((randint(0, 200) / 100) + 1) * -1
      self.dy = 0
    elif direction == 3: # down
      self.x = choice(LANES)
      self.y = -64
      self.dx = 0
      self.dy = (randint(0, 200) / 100) + 1
    else:
      self.x = choice(LANES)
      self.y = 500
      self.dx = 0
      self.dy = ((randint(0, 200) / 100) + 1) * -1