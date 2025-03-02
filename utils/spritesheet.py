import pygame as pg
import json
import os
    

class Spritesheet:
    def __init__(self, filename):
        self.img_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imgs"))
        self.filename = os.path.join(self.img_folder_path, filename)
        self.sprite_sheet = pg.image.load(self.filename).convert_alpha()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x, y, width, height):
        sprite = pg.Surface((width, height), pg.SRCALPHA)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite
    
    def parse_sprite(self, name):
        sprite = self.data['sprites'][name]
        x, y, w, h = sprite['x'], sprite['y'], sprite['width'], sprite['height']
        image = self.get_sprite(x, y, w, h)
        return image
