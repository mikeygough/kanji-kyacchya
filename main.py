# external imports
import pygame
import json
from random import randint, choice

# class imports
from Kanji import Kanji
from GameObject import GameObject

# constant imports
from constants import *

# load data
with open('./static/data.json', 'r') as file:
    data_dict = json.load(file)

# get main kanji
main_kanji = choice(data_dict['main'])
# get visually-similar kanji
similar_kanji = data_dict['similar'][main_kanji][0]

# pygame.init()
# pygame.font.init()


# # configure screen size
# screen = pygame.display.set_mode([WIDTH, HEIGHT])

# def main():
    
    