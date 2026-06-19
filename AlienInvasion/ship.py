import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen

        """Load the screen and Image and get its rect"""
        # This function return a surface representing the ship 
        self.image = pygame.image.load('images/ship.bmp')
        
        # Access the surface rect attribute 
        self.rect = self.image.get_rect() # el rectangulo es el de la imagen 
        self.screen_rect = screen.get_rect() # el rectangulo de la imagen 

        
        """Start each new ship at the bottom center of the screen"""
        self.rect.centerx = self.screen_rect.centerx # The center of the rectangle is the same as the screen 
        self.rect.bottom = self.screen_rect.bottom  # The bottom of the rect is allign with the screen bottom

        pass
    
    def blitme(self):
        """Draw the ship at its current location""" 
        self.screen.blit(self.image, self.rect)
        # Entonces para dibujar, se usa blit y requiere la imagen y el rectangulo