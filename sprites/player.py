import pygame as pg
import os
from utils.spritesheet import Spritesheet
from utils.database_logic import Hat

class Player(pg.sprite.Sprite):
    """Player class to handle player movement, animations, and interactions."""

    def __init__(self):
        """Initialize the player with default settings and load frames."""

        pg.sprite.Sprite.__init__(self)
        self.img_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imgs"))
        self.hat = Hat()
        self.hat_image1 = pg.image.load(os.path.join(self.img_folder_path, "hat1.png")).convert_alpha()
        self.hat_image2 = pg.image.load(os.path.join(self.img_folder_path, "hat2.png")).convert_alpha()
        self.startframe = pg.image.load(os.path.join(self.img_folder_path, "IdleL2.png")).convert_alpha()
        self.jumping, self.falling = False, False
        self.frame_index = 0  # Track animation frame
        self.animation_timer = 0  # Track time for animation
        self.playerleft = True # Track player direction
        self.state = 'idle' # Track state for animations
        self.on_floor = False # Track if player is on the floor for y-acceleration enabling
        self.jump_pressed = False # Disabling double jump
        self.img_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imgs"))
        self.WIDTH = 480 # Screen width
        self.HEIGHT = 600 # Screen height
        self.PLAYER_ACC = 0.5 # Player acceleration
        self.PLAYER_FRICTION = -0.12 # Player friction

        # Load the spritesheet
        self.spritesheet = Spritesheet('Playersheet.png')

        if self.hat == "0":
            self.load_character()
        if self.hat == "hat":
            self.load_hat_character()
        
        self.image = self.startframe  # Start with the first frame

        self.rect = self.image.get_rect() # Set the rect attribute for collision detection
        self.rect.center = (30, self.HEIGHT * 3/4) # Create center rect object
        self.pos = pg.Vector2(self.rect.center) # Set the position vector for movement
        self.vel = pg.Vector2(0, 0) # Set the velocity vector for movement
        self.acc = pg.Vector2(0, 0) # Set the acceleration vector for movement

        # Create hitbox for collision detection
        self.hitbox = pg.Rect(self.rect.left + 10, self.rect.top + 7, self.rect.width - 26, self.rect.height - 7)

    def update(self):
        """Update the player's position, state, and animations."""

        self.acc = pg.Vector2(0, self.PLAYER_ACC)
        self.animation_timer += 1

        keys = pg.key.get_pressed()

        if not keys[pg.K_LEFT] and not keys[pg.K_RIGHT] and self.on_floor:
            self.state = 'idle'
        
        if keys[pg.K_LEFT]:
            self.acc.x = -self.PLAYER_ACC
            self.state = 'moving'
            self.playerleft = True

        if keys[pg.K_RIGHT]:
            self.acc.x = self.PLAYER_ACC
            self.state = 'moving'
            self.playerleft = False

        if keys[pg.K_SPACE] and self.on_floor and self.vel.y == 0 and not self.jump_pressed:
            self.vel.y = -12
            self.on_floor = False
            self.jump_pressed = True

        if not keys[pg.K_SPACE]:
            self.jump_pressed = False

        if self.vel.y < 0:
            self.state = 'jumping'

        if self.vel.y > 0.5:
            self.state = 'falling'

        self.animate()

        # apply friction
        self.acc.x += self.vel.x * self.PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + self.PLAYER_ACC * self.acc
        # wrap around the sides of the screen
        if self.pos.x > self.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.WIDTH

        self.rect.midbottom = self.pos

        # Update hitbox position
        self.hitbox.topleft = (self.rect.left + 10, self.rect.top + 7)

    def animate(self):
        """Handle player animations based on the current state."""

        if self.state == 'idle':
            if self.animation_timer % 20 == 0:
                if self.playerleft:
                    self.frame_index = (self.frame_index + 1) % len(self.idle_left_frames)
                    self.image = self.idle_left_frames[self.frame_index]
                    self.animation_timer = 0
                else:
                    self.frame_index = (self.frame_index + 1) % len(self.idle_right_frames)
                    self.image = self.idle_right_frames[self.frame_index]
                    self.animation_timer = 0

        if self.state == 'moving' and not self.playerleft:
            if self.animation_timer % 6 == 0:  # Change frame every 0.1 seconds
                self.frame_index = (self.frame_index + 1) % len(self.walk_right_frames)
                self.image = self.walk_right_frames[self.frame_index]
                self.animation_timer = 0

        if self.state == 'moving' and self.playerleft:
            if self.animation_timer % 6 == 0:  # Change frame every 0.1 seconds
                self.frame_index = (self.frame_index + 1) % len(self.walk_left_frames)
                self.image = self.walk_left_frames[self.frame_index]
                self.animation_timer = 0

        if self.state == 'jumping':
            if self.playerleft:
                self.image = self.jumping_left_frames[0]
            else:
                self.image = self.jumping_right_frames[0]

        if self.state == 'falling':
            if self.playerleft:
                self.image = self.falling_left_frames[0]
            else:
                self.image = self.falling_right_frames[0]


        
    def load_character(self):
        """Load the character frames for the player without a hat."""

        self.idle_left_frames = [self.spritesheet.parse_sprite('idlel1.png'), self.spritesheet.parse_sprite('idlel2.png')]
        self.idle_right_frames = [self.spritesheet.parse_sprite('idler1.png'), self.spritesheet.parse_sprite('idler2.png')]
        self.walk_left_frames = [self.spritesheet.parse_sprite('wl1.png'), self.spritesheet.parse_sprite('wl2.png'),
                                 self.spritesheet.parse_sprite('wl3.png'), self.spritesheet.parse_sprite('wl4.png')]
        self.walk_right_frames = [self.spritesheet.parse_sprite('wr1.png'), self.spritesheet.parse_sprite('wr2.png'),
                                  self.spritesheet.parse_sprite('wr3.png'), self.spritesheet.parse_sprite('wr4.png')]
        self.jumping_left_frames = [self.spritesheet.parse_sprite('jumpingl.png')]
        self.jumping_right_frames = [self.spritesheet.parse_sprite('jumpingr.png')]
        self.falling_left_frames = [self.spritesheet.parse_sprite('fallingl.png')]
        self.falling_right_frames = [self.spritesheet.parse_sprite('fallingr.png')]

    def load_hat_character(self):
        """Load the character frames for the player with a hat."""

        self.idle_left_frames = [self.spritesheet.parse_sprite('idlel1.png'), self.spritesheet.parse_sprite('idlel2.png')]
        self.idle_right_frames = [self.spritesheet.parse_sprite('idler1.png'), self.spritesheet.parse_sprite('idler2.png')]
        self.walk_left_frames = [self.spritesheet.parse_sprite('wl1.png'), self.spritesheet.parse_sprite('wl2.png'),
                                 self.spritesheet.parse_sprite('wl3.png'), self.spritesheet.parse_sprite('wl4.png')]
        self.walk_right_frames = [self.spritesheet.parse_sprite('wr1.png'), self.spritesheet.parse_sprite('wr2.png'),
                                  self.spritesheet.parse_sprite('wr3.png'), self.spritesheet.parse_sprite('wr4.png')]
        self.jumping_left_frames = [self.spritesheet.parse_sprite('jumpingl.png')]
        self.jumping_right_frames = [self.spritesheet.parse_sprite('jumpingr.png')]
        self.falling_left_frames = [self.spritesheet.parse_sprite('fallingl.png')]
        self.falling_right_frames = [self.spritesheet.parse_sprite('fallingr.png')]

        for frame in self.idle_left_frames:
            frame.blit(self.hat_image1, (0, -8))

        for frame in self.idle_right_frames:
            frame.blit(self.hat_image1, (10, -8))

        for frame in self.walk_left_frames:
            frame.blit(self.hat_image1, (0, -8))

        for frame in self.walk_right_frames:
            frame.blit(self.hat_image1, (10, -8))

        for frame in self.jumping_left_frames:
            frame.blit(self.hat_image1, (0, -8))

        for frame in self.jumping_right_frames:
            frame.blit(self.hat_image1, (10, -8))

        for frame in self.falling_left_frames:
            frame.blit(self.hat_image1, (0, -8))

        for frame in self.falling_right_frames:
            frame.blit(self.hat_image1, (10, -8))
