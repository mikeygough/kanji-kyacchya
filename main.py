# external imports
import pygame
import json
from random import randint, choice

# class imports
from Kanji import Kanji
from GameObject import GameObject
from Player import Player
from Demon import DemonV, DemonH
from ScoreBoard import ScoreBoard

# constant imports
from constants import *

# load data
with open('./static/data.json', 'r') as file:
    data_dict = json.load(file)

# get main kanji
main_kanji = choice(data_dict['main'])
# get visually-similar kanji
similar_kanji = data_dict['similar'][main_kanji][0]

# game
pygame.init()
pygame.font.init()

# configure screen size
screen = pygame.display.set_mode([WIDTH, HEIGHT])

def main(main_kanji, similar_kanji):
    # all-sprites group
    all_sprites = pygame.sprite.Group()
    # make kanji group
    kanji_sprites = pygame.sprite.Group()
    # make demons group
    demon_sprites = pygame.sprite.Group()
    
    # make kanji instances
    main_kanji = Kanji(image=f"./static/{main_kanji}.png")
    similar_kanji = Kanji(image=f"./static/{similar_kanji}.png")

    # add to kanji group
    kanji_sprites.add(main_kanji)
    kanji_sprites.add(similar_kanji)
    
    # make player
    player = Player()

    # make demons
    demon_v = DemonV()
    demon_h = DemonH()
    
    # add to demons group
    demon_sprites.add(demon_v)
    demon_sprites.add(demon_h)
    
    # # make scoreboard
    score = ScoreBoard(30, 30, 0)
    
    # # add score to all_sprites group
    all_sprites.add(score)
    
    # add sprites to group
    all_sprites.add(main_kanji)
    all_sprites.add(similar_kanji)
    all_sprites.add(player)
    all_sprites.add(demon_v)
    all_sprites.add(demon_h)

    # get clock
    clock = pygame.time.Clock()
    
    # game loop
    running = True
    while running:
        # look at events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    player.left()
                elif event.key == pygame.K_RIGHT:
                    player.right()
                elif event.key == pygame.K_UP:
                    player.up()
                elif event.key == pygame.K_DOWN:
                    player.down()

        # Clear screen
        screen.fill((255, 255, 255))

        # Move and render Sprites
        for entity in all_sprites:
            entity.move()
            entity.render(screen)
            if entity != player:
                pass

        # Check Collisions / kanji
        kanji = pygame.sprite.spritecollideany(player, kanji_sprites)
        if kanji:
            # add validation check
            score.update(100)
            kanji.reset()

        # Check Collision / demons
        demons = pygame.sprite.spritecollideany(player, demon_sprites)
        if demons:
            running = False

        # Update the window
        pygame.display.flip()

        # tick the clock!
        clock.tick(60)


if __name__ == "__main__":
    main(main_kanji, similar_kanji)
