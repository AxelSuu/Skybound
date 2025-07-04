from utils.draw_text import draw_text
import pygame as pg
from utils.database_logic import (
    GetHighScore,
    GetScore,
    SetGamestate,
    SetLevel,
    SetHighScore,
)


""" Pause screen class to display in-game menu, missing functionality:
    - Pressable Music pause button
    - Pressable Main menu button
    - Pressable Continue button """


class Pause:
    def __init__(self, loop, main):
        self.WIDTH = 480
        self.HEIGHT = 600
        self.LIGHTBLUE = (135, 206, 235)
        self.running1 = True
        self.loop = loop
        self.main = main
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.space_pressed = False
        SetHighScore(GetScore())
        self.show_menu()

    def show_menu(self):
        while self.running1:
            self.screen.fill(self.LIGHTBLUE)
            draw_text(self.screen, "Paused", 50, self.WIDTH / 2, self.HEIGHT / 4)
            draw_text(
                self.screen, "Press V to continue", 22, self.WIDTH / 2, self.HEIGHT / 2
            )
            draw_text(
                self.screen,
                "Press Q to go to Main Menu",
                22,
                self.WIDTH / 2,
                self.HEIGHT * 3 / 4,
            )
            draw_text(
                self.screen,
                f"Highscore: {GetHighScore()}",
                22,
                self.WIDTH / 2,
                self.HEIGHT * 3 / 4 + 50,
            )
            draw_text(
                self.screen,
                f"Score: {GetScore()}",
                22,
                self.WIDTH / 2,
                self.HEIGHT * 3 / 4 + 100,
            )

            # This functionality is not implemented
            draw_text(
                self.screen,
                "space to pause music",
                22,
                self.WIDTH / 2,
                self.HEIGHT * 1 / 4 - 100,
            )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running1 = False
                    self.loop.running = False
                    SetGamestate("EXIT")
            keys = pg.key.get_pressed()
            if keys[pg.K_v]:
                self.running1 = False
                SetGamestate("GAME")
                if GetScore() == 1:
                    SetLevel(1)
                if GetScore() > 1:
                    SetLevel(2)
            if keys[pg.K_q]:
                self.running1 = False
                self.loop.running = False
                SetGamestate("MAIN_MENU")

            if keys[pg.K_SPACE] and not self.space_pressed:
                self.space_pressed = True
                if self.main.pause_music:
                    # Unpause music
                    self.main.channel3.unpause()
                    self.main.pause_music = False
                    print("Music unpaused")
                else:
                    # Pause music
                    self.main.pause_music_func()
                    self.main.pause_music = True
                    print("Music paused")
            elif not keys[pg.K_SPACE]:
                self.space_pressed = False

            pg.display.flip()
