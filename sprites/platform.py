import pygame as pg
import os


""" Class for scalable platform sprite, using pg.sprite.Sprite """


class Platform2(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.img_folder_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "imgs")
        )
        self.image = self.load_platform2(w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    """ Load platform image and importantly scale it """

    def load_platform2(self, w, h):
        image1 = pg.image.load(
            os.path.join(self.img_folder_path, "plat3.png")
        ).convert_alpha()
        return pg.transform.scale(image1, (w, h))
