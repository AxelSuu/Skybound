import pygame as pg
import numpy

from utils.database_logic import *

from windows.main_menu import *
from windows.start import *
from windows.gameover import *
from windows.paus import *
from gameloop.loop import *
from windows.new_highscore_screen import *

"""
This is the main file for the game. It is used to create screen classes and
manage the game states, as well as the music. State management is done with
the help of the database_logic.py file. The game states are: MAIN_MENU, START_SCREEN,
GAME, PAUSED, GAME_OVER, NEW_HIGHSCORE and EXIT. The database are a collection of
txt files that store state information. -> Your highscore and selected character
will be saved in the file.
"""


class Main_Loop:
    """Main loop class to manage game states and transitions."""

    def __init__(self):
        """Initialize the game and set the initial game state."""
        self.sfx_folder_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "sfxs")
        )
        pg.init()
        pg.mixer.init()
        self.pause_music = False
        self.gamesound = os.path.join(self.sfx_folder_path, "music5.ogg")
        self.menusound = os.path.join(self.sfx_folder_path, "music7.ogg")
        self.highscoresound = os.path.join(self.sfx_folder_path, "music1.ogg")
        self.channel1 = pg.mixer.Channel(0)
        self.channel2 = pg.mixer.Channel(1)
        self.channel3 = pg.mixer.Channel(2)
        self.channel4 = pg.mixer.Channel(3)
        pg.mixer.music.set_volume(0.4)
        SetGamestate(
            "MAIN_MENU"
        )  # Example of setting game state using database_logic.py
        self.current_window = None
        self.running1 = True
        self.channel1.play(pg.mixer.Sound(self.menusound), loops=-1)
        self.channel1.pause()
        self.channel3.play(pg.mixer.Sound(self.gamesound), loops=-1)
        self.channel3.pause()
        self.channel4.play(pg.mixer.Sound(self.highscoresound), loops=-1)
        self.channel4.pause()
        self.main()

    def main(self):
        """Main loop to check and transition between game states."""

        while self.running1 == True:
            current_state = GetGamestate()

            if current_state == "MAIN_MENU":
                if not isinstance(self.current_window, Main_menu):
                    if not self.pause_music:
                        self.channel1.unpause()
                    self.current_window = Main_menu()
                    self.channel1.pause()

            elif current_state == "START_SCREEN":
                if not isinstance(self.current_window, Start):
                    if not self.pause_music:
                        self.channel1.unpause()
                    self.current_window = Start()
                    self.channel1.pause()

            elif current_state == "GAME":
                if not isinstance(self.current_window, Loop):
                    if not self.pause_music:
                        self.channel3.unpause()
                    self.current_window = Loop(self)
                    self.channel3.pause()

            elif current_state == "PAUSED":
                if not isinstance(self.current_window, Pause):
                    if not self.pause_music:
                        self.channel1.unpause()
                    self.current_window = Pause(self)
                    self.channel1.pause()

            elif current_state == "GAME_OVER":
                if not isinstance(self.current_window, Gameover):
                    if not self.pause_music:
                        self.channel1.unpause()
                    self.current_window = Gameover()
                    self.channel1.pause()

            elif current_state == "NEW_HIGHSCORE":
                if not isinstance(self.current_window, NewHighscore):
                    if not self.pause_music:
                        self.channel4.unpause()
                    self.current_window = NewHighscore()
                    self.channel4.pause()

            elif current_state == "EXIT":
                self.running1 = False
                pg.mixer.music.stop()
                pg.quit()

    # This functionality was never implemented (pause screen was never finished)
    def pause_music_func(self):
        """Pause the music."""
        self.pausemusic = True
        self.channel1.pause()
        self.channel2.pause()
        self.channel3.pause()
        self.channel4.pause()


if __name__ == "__main__":
    Main_Loop()
