import pygame
from pygame.sprite import Sprite 


class Alien(Sprite):
    """Class to manage aliens"""

    def __init__(self, ai_game):
        """Initialize alien and its starting positiion"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alienship.bmp')
        self.rect = self.image.get_rect()

        #start all new aliens to the top of the screen 
        self.rect.x = self.rect.width
        self.rect.y - self.rect.height

        #store the aliens exact horizontal position
        self.x = float(self.rect.x)

        
    def check_edges(self):
        """return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        return(self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

