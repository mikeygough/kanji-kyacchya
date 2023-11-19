# KanjiBoard
import pygame

class KanjiBoard(pygame.sprite.Sprite):
    def __init__(self, x, y, kanji):
        super().__init__()
        self.kanji = kanji
        self.font = pygame.font.Font('./static/hiragino-W5.ttc', 30)
        self.surf = self.font.render(f"{self.kanji}", False, (0, 0, 0))
        self.dx = 0
        self.dy = 0
        self.x = x
        self.y = y
        
    def update(self, kanji):
        self.kanji = kanji
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def render(self, screen):
        self.surf = self.font.render(f"{self.kanji}", False, (0, 0, 0))
        screen.blit(self.surf, (self.x, self.y))
    
    def reset(self):
        pass