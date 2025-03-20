import pygame as pg
import os

""" Class for pause button sprite, using pg.sprite.Sprite
    sits topleft on screen, able to create pausescreen"""


class Closebutton(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.img_folder_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "imgs")
        )
        self.image = pg.image.load(
            os.path.join(self.img_folder_path, "paus.png")
        ).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
