import pygame as pg
import os

# This file was not implemented, boilerplate code for Spritesheet class

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        img_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img"))
        self.sprite_sheet = pg.image.load(os.path.join(img_folder_path, filename)).convert_alpha()


    def get_sprite(self, x, y, w, h):
        sprite = pg.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        return sprite