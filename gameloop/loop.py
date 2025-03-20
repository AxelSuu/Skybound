import pygame as pg
import os
from levels.level1 import LevelClass
from utils.database_logic import *
from windows.paus import Pause

# Constants
WIDTH : int = 480
HEIGHT : int = 600
FPS : int = 100
TITLE : str = "Skybound"
WHITE : tuple = (255, 255, 255)
IMG_FOLDER_PATH : str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imgs"))

class Loop():
    def __init__(self, main):
        self.main = main
        self.screen = None
        self.clock = None
        self.bg_scroll = 0
        self.running = True
        self.level = None
        self.background = None
        self.background2 = None
        self.mouse = None
        self.click = None
        self.init_pygame()
        self.startgame()

    def init_pygame(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        icon = pg.image.load(os.path.join(IMG_FOLDER_PATH, 'icon.png'))
        pg.display.set_icon(icon)
        self.clock = pg.time.Clock()

    def startgame(self):
        self.level = LevelClass(self)
        self.load_level()
        self.run()

    def load_level(self):
        if GetLevel() == 1:
            self.level.level1()
        elif GetLevel() > 1:
            self.level.level2()
        self.background = self.level.sky
        self.background2 = pg.transform.flip(self.background, True, False).convert()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                SetGamestate("EXIT")

    def update(self):
        self.all_sprites.update()
        self.handle_collisions()

    def handle_collisions(self):
        # Player platform collision
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits and self.player.vel.y >= 0:
            self.player.pos.y = hits[0].rect.top - 1
            self.player.vel.y = 0
            self.player.on_floor = True

        # Mob platform collision
        hits2 = pg.sprite.spritecollide(self.mob, self.platforms, False)
        if hits2:
            if self.mob.vel.y > 0 and not self.mob.on_floor:
                self.mob.pos.y = hits2[0].rect.top
                self.mob.vel.y = 0
                self.mob.on_floor = True

        # Player goal collision
        win = pg.sprite.spritecollide(self.player, self.goals, False)
        if win:
            SetHighScore(GetScore())
            SetScore(GetScore() + 1)
            self.running = False
            if GetScore() > GetHighScore() and GetScore() > 2:
                SetGamestate("NEW_HIGHSCORE")
            else:
                SetGamestate("GAME_OVER")

        # Player mob collision
        end2 = pg.sprite.spritecollide(self.player, self.mobs, False)
        if end2:
            self.running = False
            SetScore(1)
            SetGamestate("GAME_OVER")

        # Mouse pause button collision
        self.mouse = pg.mouse.get_pos()
        self.click = pg.mouse.get_pressed()
        if (self.closebutton.rect.x + 50 > self.mouse[0] > self.closebutton.rect.x and
                self.closebutton.rect.y + 50 > self.mouse[1] > self.closebutton.rect.y):
            if self.click[0] == 1:
                Pause(self)

        # Mob AI logic
        if self.player.pos.x < self.mob.pos.x:
            self.mob.vel.x = -1.4
        if self.player.pos.x > self.mob.pos.x:
            self.mob.vel.x = 1.4
        if self.player.pos.y + 40 < self.mob.pos.y and self.mob.on_floor:
            self.mob.vel.y = -10
            self.mob.on_floor = False
        if self.mob.on_floor and self.mob.vel.y != 0:
            self.mob.on_floor = False

    def draw(self):
        self.screen.fill(WHITE)
        self.bg_scroll += 1.5
        if self.bg_scroll >= self.background.get_width():
            self.bg_scroll = 0
            self.background = pg.transform.flip(self.background, True, False).convert()
            self.background2 = pg.transform.flip(self.background2, True, False).convert()
        self.screen.blit(self.background, (WIDTH - self.background.get_width() + self.bg_scroll, 0))
        if self.bg_scroll > self.background.get_width() - WIDTH:
            self.screen.blit(self.background2, (WIDTH - self.background.get_width() * 2 + self.bg_scroll, 0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()