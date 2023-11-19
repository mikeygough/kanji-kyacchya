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
from KanjiBoard import KanjiBoard

# constant imports
from constants import *

# load data
with open('./static/data.json', 'r') as file:
    data_dict = json.load(file)

# get main kanji
main_k = choice(data_dict['main'])
# get visually-similar kanji
similar_k = data_dict['similar'][main_k][0]

# game
pygame.init()
pygame.font.init()

# configure screen size
screen = pygame.display.set_mode([WIDTH, HEIGHT])

def main(main_k, similar_k):
    # all-sprites group
    all_sprites = pygame.sprite.Group()
    # make demons group
    demon_sprites = pygame.sprite.Group()
    
    # make kanji instances
    main_kanji = Kanji(image=f"./static/{main_k}.png")
    similar_kanji = Kanji(image=f"./static/{similar_k}.png")
    
    # make player
    player = Player()

    # make demons
    demon_v = DemonV()
    demon_h = DemonH()
    
    # add to demons group
    demon_sprites.add(demon_v)
    demon_sprites.add(demon_h)
    
    # make scoreboard
    score = ScoreBoard(30, 30, 0)
    # make kanjiboard
    kanji_board = KanjiBoard(60, 35, main_k)
    
    # add score & kanjiboard to all_sprites group
    all_sprites.add(score)
    all_sprites.add(kanji_board)
    
    
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

        # Check Collision / main kanji
        if pygame.sprite.collide_rect(player, main_kanji):
            # correct, kill current kanji
            main_kanji.kill()
            similar_kanji.kill()
            
            # get main kanji
            main_k = choice(data_dict['main'])
            # get visually-similar kanji
            similar_k = data_dict['similar'][main_k][0]
            
            # make kanji instances
            main_kanji = Kanji(image=f"./static/{main_k}.png")
            similar_kanji = Kanji(image=f"./static/{similar_k}.png")

            # add to all_sprites group
            all_sprites.add(main_kanji)
            all_sprites.add(similar_kanji)
            
            # update score
            score.update(1)
            # update kanjiboard
            kanji_board.update(main_k)
        
        # Check Collisions / similar kanji
        if pygame.sprite.collide_rect(player, similar_kanji):
            running = False
            print("Wrong Kanji!")

        # Check Collision / demons
        demons = pygame.sprite.spritecollideany(player, demon_sprites)
        if demons:
            running = False
            print("Ouch, demon!")

        # Update the window
        pygame.display.flip()

        # tick the clock!
        clock.tick(60)


if __name__ == "__main__":
    main(main_k, similar_k)
