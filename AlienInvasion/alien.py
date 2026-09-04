import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings 

        """Load the alien image and set its rect attribute"""
        # This function return a surface representing the ship 
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect() # el rectangulo es el de la imagen 
        
        # Place it near the top left corner of the screen , adding a spce 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x  = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location""" 
        self.screen.blit(self.image, self.rect)
        # Entonces para dibujar, se usa blit y requiere la imagen y el rectangulo

    def update(self, deltaTime):
        self.x += self.ai_settings.alien_speed *self.ai_settings.fleet_direction* deltaTime
        self.rect.centerx = self.x
        

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right or self.rect.left <= 0)