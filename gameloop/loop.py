import pygame as pg
import os
from levels.level1 import LevelClass
from utils.database_logic import *
from windows.paus import Pause

''' Main game loop class, handles game logic and game states
    starts with creating the screen and level instance, then
    runs the game loop. '''
class Loop():
    def __init__(self, main):
        # initialize game window, etc
        self.main = main
        self.WIDTH = 480
        self.HEIGHT = 600
        self.FPS = 100
        self.TITLE = "Skybound"
        self.WHITE = (255, 255, 255)
        self.img_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imgs"))
        self.startgame()

    def startgame(self):
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption(self.TITLE)
        icon = pg.image.load(os.path.join(self.img_folder_path, 'icon.png'))
        pg.display.set_icon(icon)
        self.clock = pg.time.Clock()
        self.bg_scroll = 0

        self.running = True
        # Create level instance
        self.level = LevelClass(self)
        if GetLevel() == 1: # Database logic example
            self.level.level1()
        elif GetLevel() > 1: # Database logic example
            self.level.level2()
        self.background = self.level.sky

        # Game Loop
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            # Updating all sprites here
            self.all_sprites.update()

            # Player platform collision
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits and self.player.vel.y >= 0:
                self.player.pos.y = hits[0].rect.top -1
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
                SetHighScore(GetScore()) # Database logic example
                SetScore(GetScore() + 1) # Database logic example
                self.running = False
                if GetScore() > GetHighScore() and GetScore() > 2: # Database logic example
                    SetGamestate("NEW_HIGHSCORE") # Database logic example
                else:         
                    SetGamestate("GAME_OVER") # Database logic example
            
            # Player mob collision
            end2 = pg.sprite.spritecollide(self.player, self.mobs, False)
            if end2:
                self.running = False
                SetScore(1) # Database logic example
                SetGamestate("GAME_OVER") # Database logic example
            
            # Mouse pausebutton collision
            self.mouse = pg.mouse.get_pos()
            self.click = pg.mouse.get_pressed()
            if self.closebutton.rect.x + 50 > self.mouse[0] > self.closebutton.rect.x and self.closebutton.rect.y + 50 > self.mouse[1] > self.closebutton.rect.y:
                if self.click[0] == 1:
                    Pause(self)
            
            
            # Mob AI logic
            if self.player.pos.x < self.mob.pos.x:
                self.mob.vel.x = -1.4
            if self.player.pos.x > self.mob.pos.x:
                self.mob.vel.x = 1.4
            if self.player.pos.y + 40 < self.mob.pos.y and self.mob.on_floor == True:
                self.mob.vel.y = -10
                self.mob.on_floor = False
            if self.mob.on_floor and self.mob.vel.y != 0:
                self.mob.on_floor = False

            # check for closing window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    SetGamestate("EXIT")
                        

            # Game Loop - draw
            self.screen.fill(self.WHITE)
            self.bg_scroll += 1.5
            if self.bg_scroll >= self.background.get_width() - 480:
                self.bg_scroll = 0
            self.screen.blit(self.background, (480 - self.background.get_width() + self.bg_scroll, 0))
            self.all_sprites.draw(self.screen)

            # *after* drawing everything, flip the display
            pg.display.flip()
