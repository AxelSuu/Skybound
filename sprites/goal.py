import pygame as pg
import os

''' Very similiar to pausebutton sprite'''
class Goal(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.img_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imgs"))
        self.image = pg.image.load(os.path.join(self.img_folder_path, "goal2.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y