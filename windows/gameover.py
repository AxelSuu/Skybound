import pygame as pg
from utils.draw_text import draw_text
from utils.database_logic import GetHighScore, GetScore, SetGamestate, SetLevel


""" General gameover screen when player dies or wins the game."""


class Gameover:
    def __init__(self):
        self.WIDTH = 480
        self.HEIGHT = 600
        self.LIGHTBLUE = (135, 206, 235)
        self.on_gameover = True
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.show_go_screen()

    def show_go_screen(self):
        while self.on_gameover:
            self.screen.fill(self.LIGHTBLUE)

            draw_text(
                self.screen,
                f"Press V to play Level {GetScore()}",
                22,
                self.WIDTH / 2,
                self.HEIGHT * 2 / 4,
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
                self.HEIGHT * 1 / 4,
            )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.on_gameover = False
                    SetGamestate("EXIT")
            keys = pg.key.get_pressed()
            if keys[pg.K_v]:
                self.on_gameover = False
                if GetScore() == 1:
                    SetLevel(1)
                if GetScore() > 1:
                    SetLevel(2)
                SetGamestate("GAME")
            if keys[pg.K_q]:
                self.on_gameover = False
                SetGamestate("MAIN_MENU")

            pg.display.flip()
