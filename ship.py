import pygame

class Ship:
    """class to manage the ship"""

    def __init__(self, ai_game):
        """initilize the ship and set the starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings= ai_game.settings

        #loads ship image and gets its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom


        self.x = float(self.rect.x)

        #movement flag start with a ship that aint move
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position on movement flag"""
        #update the ships x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update the rect object from self.x
        self.rect.x = self.x
    def blitime(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    