import pygame as pg
import os

# from sprites.player import Player
from sprites.player import Player
from sprites.platform import Platform2
from sprites.goal import Goal
from sprites.mob import Mob
from sprites.pausebutton import Closebutton

import random

""" Responsible for creating the level in the init of the game loop
    creates sprite instances and adds them to the allsprite class
    for collision detection and rendering.
    Level 1 is a static level, subsequent levels are randomly generated
    with careful consideration to ensure that the level is 
    enjoyable and completable. """


class LevelClass:
    def __init__(self, game):
        self.img_folder_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "imgs")
        )
        self.WIDTH = 480
        self.HEIGHT = 600
        self.skys = [
            pg.image.load(
                os.path.join(self.img_folder_path, "sky2.png")
            ).convert_alpha(),
            pg.image.load(
                os.path.join(self.img_folder_path, "Freesky5.png")
            ).convert_alpha(),
            pg.image.load(
                os.path.join(self.img_folder_path, "Freesky2.png")
            ).convert_alpha(),
            pg.image.load(
                os.path.join(self.img_folder_path, "Freesky3.png")
            ).convert_alpha(),
            pg.image.load(
                os.path.join(self.img_folder_path, "Freesky4.png")
            ).convert_alpha(),
            pg.image.load(
                os.path.join(self.img_folder_path, "Freesky14.png")
            ).convert_alpha(),
            pg.image.load(
                os.path.join(self.img_folder_path, "Freesky15.png")
            ).convert_alpha(),
            pg.image.load(
                os.path.join(self.img_folder_path, "Freesky7.png")
            ).convert_alpha(),
            pg.image.load(
                os.path.join(self.img_folder_path, "Freesky8.png")
            ).convert_alpha(),
        ]
        self.sky = self.skys[0]
        self.game = game

    def level1(self):
        # Create level 1 (static)
        self.game.all_sprites = pg.sprite.Group()
        self.game.platforms = pg.sprite.Group()
        self.game.goals = pg.sprite.Group()
        self.game.player = Player()
        self.game.all_sprites.add(self.game.player)
        self.game.closebutton = Closebutton(10, 10, 50, 50)
        self.game.all_sprites.add(self.game.closebutton)
        self.game.mobs = pg.sprite.Group()
        self.game.mob = Mob()
        self.game.all_sprites.add(self.game.mob)
        self.game.mobs.add(self.game.mob)

        p1 = Platform2(0, self.HEIGHT - 40, self.WIDTH, 40)
        self.game.all_sprites.add(p1)
        self.game.platforms.add(p1)
        p2 = Platform2(self.WIDTH / 2 - 50, self.HEIGHT * 3 / 4, 100, 20)
        self.game.all_sprites.add(p2)
        self.game.platforms.add(p2)
        p3 = Platform2(self.WIDTH / 2 - 150, self.HEIGHT * 3 / 6, 100, 20)
        self.game.all_sprites.add(p3)
        self.game.platforms.add(p3)
        p4 = Platform2(self.WIDTH / 2 + 100, self.HEIGHT * 3 / 9, 100, 20)
        self.game.all_sprites.add(p4)
        self.game.platforms.add(p4)
        p5 = Platform2(self.WIDTH / 2 - 100, 100, 100, 20)
        self.game.all_sprites.add(p5)
        self.game.platforms.add(p5)
        goal = Goal(self.WIDTH / 2 - 100, 60, 20, 20)
        self.game.all_sprites.add(goal)
        self.game.goals.add(goal)

    def level2(self):
        # Create level 2 (randomly generated)
        self.sky = random.choice(self.skys)
        self.game.all_sprites = pg.sprite.Group()
        self.game.platforms = pg.sprite.Group()
        self.game.goals = pg.sprite.Group()
        self.game.player = Player()
        self.game.all_sprites.add(self.game.player)
        self.game.closebutton = Closebutton(10, 10, 50, 50)
        self.game.all_sprites.add(self.game.closebutton)
        self.game.mobs = pg.sprite.Group()
        self.game.mob = Mob()
        self.game.all_sprites.add(self.game.mob)
        self.game.mobs.add(self.game.mob)

        # Create floor Platform
        p1 = Platform2(0, self.HEIGHT - 40, self.WIDTH, 40)
        self.game.all_sprites.add(p1)
        self.game.platforms.add(p1)

        # Create random platforms
        num_platforms = 4
        platforms = []
        for plat in range(num_platforms):
            width = random.randint(50, 100)
            height = 20
            x = random.randint(0, self.WIDTH - width)
            y = random.randint(40, self.WIDTH - height - 300)
            platform = Platform2(x, y, width, height)
            platforms.append(platform)

        # Sort platforms by y-coordinate
        platforms.sort(key=lambda p: p.rect.y)

        # Adjust y-coordinates to ensure maximum 200 pixels between platforms
        for i in range(1, len(platforms)):
            if platforms[i].rect.y - platforms[i - 1].rect.y > 200:
                platforms[i].rect.y = platforms[i - 1].rect.y + 200

        # Adjust y-coordinates to ensure minimum 150 pixels between platforms
        for i in range(1, len(platforms)):
            if platforms[i].rect.y - platforms[i - 1].rect.y < 150:
                platforms[i].rect.y = platforms[i - 1].rect.y + 150

        # Adjust x-coordinates to ensure minimum 100 pixels between platforms
        for i in range(1, len(platforms)):
            if abs(platforms[i].rect.x - platforms[i - 1].rect.x) < 100:
                if platforms[i].rect.x < platforms[i - 1].rect.x:
                    platforms[i].rect.x -= 100
                else:
                    platforms[i].rect.x += 100

        # final check to see if a platform has been placed too far down
        for i in range(1, len(platforms)):
            if platforms[i].rect.y > self.HEIGHT - 160:
                platforms[i].rect.y = self.HEIGHT - 160

        # check to see if a platform has been placed outside of the width
        for i in range(1, len(platforms)):
            if platforms[i].rect.x > self.WIDTH - 80:
                platforms[i].rect.x = self.WIDTH - 80
            if platforms[i].rect.x < 0:
                platforms[i].rect.x = 0

        # Add platforms to the game
        for platform in platforms:
            self.game.all_sprites.add(platform)
            self.game.platforms.add(platform)

        # Place the goal on a random platform
        goal_platform = platforms[0]
        goal_x = goal_platform.rect.centerx - 10
        goal_y = goal_platform.rect.top - 20

        # Ensure the goal is within screen boundaries
        if goal_x < 0:
            goal_x = 0
        if goal_x > self.WIDTH - 20:
            goal_x = self.WIDTH - 20
        if goal_y < 0:
            goal_y = 0
        if goal_y > self.HEIGHT - 60:
            goal_y = self.HEIGHT - 60

        goal = Goal(goal_x, goal_y, 20, 20)
        self.game.all_sprites.add(goal)
        self.game.goals.add(goal)
