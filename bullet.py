
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):

    def __init__(self, ai_game):
        """make a bullet class that you can manage"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        

        #make a bullet rect(AKA rectangle) at (0,0) then set the right position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullets positon as float
        self.y = float(self.rect.y)

    def update(self):
        """move th bullet on the screen"""
        #updates the exact bullet position
        self.y -= self.settings.bullet_speed
        #update the rect positon
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)