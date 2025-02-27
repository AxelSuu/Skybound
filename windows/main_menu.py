import pygame as pg
import os
from utils.draw_text import draw_text
from utils.database_logic import GetHighScore, SetGamestate, SetHat, SetChar, manualSetHighScore, SelectedChar, Hat


''' Main menu screen with buttons to shop, character selection, highscore and start game.
    Missing functionality:
    - Buy hat
    - character selection functionality'''
class Main_menu():
    def __init__(self):
        self.WIDTH = 480
        self.HEIGHT = 600
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.LIGHTBLUE = (135, 206, 235)
        self.BLUE = (0, 0, 255)
        self.TITLE = "Skybound"
        self.img_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imgs"))

        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption(self.TITLE)
        icon = pg.image.load(os.path.join(self.img_folder_path, 'icon.png'))
        self.bg_scroll = 0
        self.background = pg.image.load(os.path.join(self.img_folder_path, 'Sky2.png')).convert()
        self.background2 = pg.transform.flip(self.background, True, False).convert()
        pg.display.set_icon(icon)
        self.main_menu()

    def main_menu(self):
        main_menu = True
        while main_menu:

            # Background animation block
            self.screen.fill(self.WHITE)
            self.bg_scroll += 0.5
            if self.bg_scroll >= self.background.get_width():
                self.bg_scroll = 0
                self.background = pg.transform.flip(self.background, True, False).convert()
                self.background2 = pg.transform.flip(self.background2, True, False).convert()
            self.screen.blit(self.background, (480 - self.background.get_width() + self.bg_scroll, 0))
            if self.bg_scroll > self.background.get_width() - 480:
                self.screen.blit(self.background2, (480 -self.background.get_width()*2 + self.bg_scroll, 0))

            # Text block
            draw_text(self.screen, "Skybound", 50, self.WIDTH / 2, self.HEIGHT / 4)
            draw_text(self.screen, "Press Space to play", 22, self.WIDTH / 2, self.HEIGHT / 2)
            draw_text(self.screen, "Shop", 22, self.WIDTH / 2, self.HEIGHT * 3 / 4 - 10)
            draw_text(self.screen, "Character Selection", 22, self.WIDTH / 2, self.HEIGHT * 3 / 4 + 40)
            draw_text(self.screen, f"Highscore: {GetHighScore()}", 22, self.WIDTH / 2, self.HEIGHT * 3 / 4 + 100)
            draw_text(self.screen, "Restart", 22, self.WIDTH / 2, 40)
        
            # Event handler
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    main_menu = False
                    SetGamestate("EXIT")
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    if self.shop_button.collidepoint(mouse_pos):
                        self.show_shop()
                    if self.character_button.collidepoint(mouse_pos):
                        self.show_character_selection()
                    if self.restart_button.collidepoint(mouse_pos):
                        manualSetHighScore(0)
                        SetHat("0")
                        SetChar("0")
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                main_menu = False
                SetGamestate("START_SCREEN")

            # Draw buttons block
            self.shop_button = pg.Rect(self.WIDTH / 2 - 50, self.HEIGHT * 3 / 4 - 10, 100, 30)
            self.character_button = pg.Rect(self.WIDTH / 2 - 100, self.HEIGHT * 3 / 4 + 40, 200, 30)
            self.restart_button = pg.Rect(self.WIDTH / 2 - 50, 40, 100, 30)
            pg.draw.rect(self.screen, self.BLACK, self.shop_button, 2)
            pg.draw.rect(self.screen, self.BLACK, self.character_button, 2)
            pg.draw.rect(self.screen, self.BLACK, self.restart_button, 2)

            pg.display.flip()

    def show_shop(self):
        # Create shop screen, should maybe be its own class
        # Functionality not implemented
        shop_screen = True
        hat_image = pg.image.load(os.path.join(self.img_folder_path, "hat1.png")).convert_alpha()
        self.hat_status = 0
        while shop_screen:
            self.screen.fill(self.LIGHTBLUE)
            self.screen.blit(hat_image, (self.WIDTH / 2 - 100, self.HEIGHT / 2))
            draw_text(self.screen, "Shop, hat costs 20", 50, self.WIDTH / 2, self.HEIGHT / 4)
            draw_text(self.screen, f"Coins: {GetHighScore()}", 22, self.WIDTH / 2, self.HEIGHT / 2 - 50)
            draw_text(self.screen, "Buy hat", 22, self.WIDTH / 2, self.HEIGHT / 2 - 10)
            draw_text(self.screen, "Press ESC to return", 22, self.WIDTH / 2, self.HEIGHT * 0.8)
            if self.hat_status == 1:
                draw_text(self.screen, "You bought a red hat!", 22, self.WIDTH / 2, self.HEIGHT / 2 + 50)
            if self.hat_status == 2:
                draw_text(self.screen, "You don't have enough coins!", 22, self.WIDTH / 2, self.HEIGHT / 2 + 50)
            if self.hat_status == 3:
                draw_text(self.screen, "You already have a red hat!", 22, self.WIDTH / 2, self.HEIGHT / 2 + 50)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    shop_screen = False
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    shop_screen = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    if self.buy_button.collidepoint(mouse_pos):
                        self.buy()
            
            self.buy_button = pg.Rect(self.WIDTH / 2 - 50, self.HEIGHT / 2 - 10, 100, 30)
            pg.draw.rect(self.screen, self.BLACK, self.buy_button, 2)

            pg.display.flip()

    def buy(self):
        # This function is not implemented, but should be implemented to buy hats
        # Implemented with database logic and hat blit should be added to player class
        pass
        '''
        if GetHighScore() >= 20 and Hat() != "red":
            SetHighScore(GetHighScore() - 20)
            self.hat_status = 1
            SetHat("red")
        if GetHighScore() < 20:
            self.hat_status = 2
        if Hat() == "red":
            self.hat_status = 3'''

    def show_character_selection(self):
        # Create character selection screen
        # Should maybe be its own class
        # Functionality not implemented in player class

        hat_image = pg.image.load(os.path.join(self.img_folder_path, "hat1.png")).convert_alpha()
        normal_image = pg.image.load(os.path.join(self.img_folder_path, "char4.png")).convert_alpha()
        hat_character = normal_image.copy()
        hat_character.blit(hat_image, (0, 0))

        character_screen = True
        while character_screen:
            self.screen.fill(self.LIGHTBLUE)
            draw_text(self.screen, "Character Selection", 50, self.WIDTH / 2, self.HEIGHT / 4)
            draw_text(self.screen, "Press ESC to return", 22, self.WIDTH / 2, self.HEIGHT * 0.8)

            # Draw buttons
            self.hat_button = pg.Rect(self.WIDTH / 2 - 50, self.HEIGHT / 2 - 10, 100, 30)
            self.normal_button = pg.Rect(self.WIDTH / 2 - 50, self.HEIGHT / 2 + 40, 100, 30)

            selected_char = SelectedChar()
            if selected_char == 0:
                pg.draw.rect(self.screen, self.BLUE, self.normal_button)
                pg.draw.rect(self.screen, self.BLACK, self.hat_button, 2)
                draw_text(self.screen, "Normal", 22, self.WIDTH / 2, self.HEIGHT / 2 + 40)
                draw_text(self.screen, "Hat", 22, self.WIDTH / 2, self.HEIGHT / 2 - 10)
                self.screen.blit(normal_image, (self.WIDTH / 2 + 100, self.HEIGHT / 2 - 50))

            elif selected_char == 1:
                pg.draw.rect(self.screen, self.BLUE, self.hat_button)
                pg.draw.rect(self.screen, self.BLACK, self.normal_button, 2)
                draw_text(self.screen, "Normal", 22, self.WIDTH / 2, self.HEIGHT / 2 + 40)
                draw_text(self.screen, "Hat", 22, self.WIDTH / 2, self.HEIGHT / 2 - 10)
                self.screen.blit(hat_character, (self.WIDTH / 2 + 100, self.HEIGHT / 2 - 50))

            else:
                pg.draw.rect(self.screen, self.BLACK, self.hat_button, 2)
                pg.draw.rect(self.screen, self.BLACK, self.normal_button, 2)
                draw_text(self.screen, "Normal", 22, self.WIDTH / 2, self.HEIGHT / 2 + 40)
                draw_text(self.screen, "Hat", 22, self.WIDTH / 2, self.HEIGHT / 2 - 10)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    character_screen = False
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    character_screen = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    if self.hat_button.collidepoint(mouse_pos) and Hat() == "red":
                        SetChar("1")
                    if self.normal_button.collidepoint(mouse_pos):
                        SetChar("0")

            pg.display.flip()
