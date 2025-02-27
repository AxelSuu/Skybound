import pygame as pg
import os

''' Class for mob sprite, using pg.sprite.Sprite
    Very based on player sprite'''
class Mob(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.img_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imgs"))
        self.HEIGHT = 600
        self.WIDTH = 480
        self.MOB_ACC = 0.5
        self.MOB_FRICTION = -0.12
        self.walk_frames = [
            pg.image.load(os.path.join(self.img_folder_path, 'Mob3 - kopia.png')).convert_alpha(),
            pg.image.load(os.path.join(self.img_folder_path, 'Mob3_1.png')).convert_alpha(),
            pg.image.load(os.path.join(self.img_folder_path, 'Mob3.png')).convert_alpha(),
            pg.image.load(os.path.join(self.img_folder_path, 'Mob3_3.png')).convert_alpha()
        ]
        self.image = self.walk_frames[0]  # Start with the first frame
        self.frame_index = 0  # Track animation frame
        self.animation_timer = 0  # Track time for animation

        self.rect = self.image.get_rect()
        self.rect.center = (440, self.HEIGHT * 3/4 +10)
        self.pos = pg.Vector2(self.rect.center)
        self.vel = pg.Vector2(0, 0)
        self.acc = pg.Vector2(0, 0)
        self.on_floor = False

        self.hitbox = pg.Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)

    def update(self):
        self.acc = pg.Vector2(0, self.MOB_ACC)
        
        
        self.animation_timer += 2

        if self.animation_timer % 10 == 0:

            self.frame_index = (self.frame_index + 1) % len(self.walk_frames)
            self.image = self.walk_frames[self.frame_index]

        # apply friction
        self.acc.x += self.vel.x * self.MOB_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + self.MOB_ACC * self.acc
        # wrap around the sides of the screen
        if self.pos.x > self.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.WIDTH

        self.rect.midbottom = self.pos

        # Update hitbox position
        self.hitbox.topleft = (self.rect.left, self.rect.top)