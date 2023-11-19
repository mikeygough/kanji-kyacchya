# Apple
from GameObject import GameObject
from constants import LANES
from random import randint, choice

class DemonV(GameObject):
  def __init__(self):
    super().__init__(0, 0, './static/demon.png')
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
    
class DemonH(GameObject):
  def __init__(self):
    super().__init__(0, 0, './static/demon.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500:
      self.reset()

  def reset(self):
    self.x = -64
    self.y = choice(LANES)