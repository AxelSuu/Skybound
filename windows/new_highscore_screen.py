import pygame as pg
import os
from utils.draw_text import draw_text
from utils.database_logic import GetHighScore, GetScore, SetGamestate, SetLevel


""" Only called when score > highscore for dopamine rush."""


class NewHighscore:
    def __init__(self):
        self.WIDTH = 480
        self.HEIGHT = 600
        self.WHITE = (255, 255, 255)
        self.img_folder_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "imgs")
        )
        self.on_NH = True
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.bg_scroll = 0
        self.background = pg.image.load(
            os.path.join(self.img_folder_path, "Sky2.png")
        ).convert()
        self.background2 = pg.transform.flip(self.background, True, False).convert()
        self.show_NH_screen()

    def show_NH_screen(self):
        while self.on_NH:
            self.screen.fill(self.WHITE)
            self.bg_scroll += 0.5
            if self.bg_scroll >= self.background.get_width():
                self.bg_scroll = 0
                self.background = pg.transform.flip(
                    self.background, True, False
                ).convert()
                self.background2 = pg.transform.flip(
                    self.background2, True, False
                ).convert()
            self.screen.blit(
                self.background, (480 - self.background.get_width() + self.bg_scroll, 0)
            )
            if self.bg_scroll > self.background.get_width() - 480:
                self.screen.blit(
                    self.background2,
                    (480 - self.background.get_width() * 2 + self.bg_scroll, 0),
                )

            draw_text(
                self.screen,
                f"Press V to play Level {GetScore()}",
                22,
                self.WIDTH / 2,
                self.HEIGHT * 2 / 4,
            )  # {Loop.levelcounter}
            draw_text(
                self.screen,
                "Press Q to go to Main Menu",
                22,
                self.WIDTH / 2,
                self.HEIGHT * 3 / 4,
            )
            draw_text(
                self.screen, f"New Highscore!!", 50, self.WIDTH / 2, self.HEIGHT * 1 / 4
            )
            draw_text(
                self.screen,
                f"Highscore: {GetHighScore()}",
                30,
                self.WIDTH / 2,
                self.HEIGHT * 1 / 4 + 70,
            )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.on_NH = False
                    SetGamestate("EXIT")
            keys = pg.key.get_pressed()
            if keys[pg.K_v]:
                self.on_NH = False
                if GetScore() == 1:
                    SetLevel(1)
                if GetScore() > 1:
                    SetLevel(2)
                SetGamestate("GAME")
            if keys[pg.K_q]:
                self.on_NH = False
                SetGamestate("MAIN_MENU")

            pg.display.flip()
