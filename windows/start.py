import pygame as pg
from utils.draw_text import draw_text
from utils.database_logic import (
    GetHighScore,
    SetGamestate,
    SetScore,
    SetLevel,
    GetScore,
)

import string
import time
import random

""" Start screen class to display the start screen and game instructions
    for buffering between menu and the game."""


class Start:
    def __init__(self):
        self.WIDTH = 480
        self.HEIGHT = 600
        self.LIGHTBLUE = (135, 206, 235)
        self.OnstartScreen = True
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.start_screen()

    def start_screen(self):

        # This block is for a cool start screen dev message
        if GetHighScore() == 0:
            self.screen.fill(self.LIGHTBLUE)
            text = string.ascii_letters + " " + "!" + "/"
            target = "Hello /Axel"
            result = ""
            for letter in target:
                while True:
                    I = random.choice(text)
                    self.screen.fill(self.LIGHTBLUE)
                    time.sleep(0.01)
                    draw_text(
                        self.screen, result + I, 50, self.WIDTH / 2, self.HEIGHT / 4
                    )
                    pg.display.flip()
                    if I == letter:
                        result += I
                        break
                    time.sleep(0.000001)
                time.sleep(0.000001)
            time.sleep(0.5)

        # The actual start screen loop
        while self.OnstartScreen:
            self.screen.fill(self.LIGHTBLUE)

            draw_text(
                self.screen, "Escape the monster", 50, self.WIDTH / 2, self.HEIGHT / 4
            )
            draw_text(
                self.screen,
                "Arrow keys to move, Space to jump",
                22,
                self.WIDTH / 2,
                self.HEIGHT / 2,
            )
            draw_text(
                self.screen, "Press V to play", 22, self.WIDTH / 2, self.HEIGHT * 3 / 4
            )
            draw_text(
                self.screen,
                f"Highscore: {GetHighScore()}",
                22,
                self.WIDTH / 2,
                self.HEIGHT * 3 / 4 + 50,
            )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.OnstartScreen = False
                    SetGamestate("EXIT")
            keys = pg.key.get_pressed()
            if keys[pg.K_v]:
                self.OnstartScreen = False
                SetGamestate("GAME")
                SetScore(1)
                SetLevel(1)

            pg.display.flip()
