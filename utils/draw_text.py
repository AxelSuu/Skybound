import pygame as pg
import os


''' Function to draw text on screen with string, size, x and y position for
    rectangle midtop. Font: Outfit, color: black '''
def draw_text(screen, text, size, x, y):
    font_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "font", "Outfit-Regular.ttf"))
    BLACK = (0, 0, 0)
    font = pg.font.Font(font_folder_path, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)