import pygame 

from pygame.sprite import Sprite

# Bullet inherit from Sprite 
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__() # This constructor has to be explicit 
        # tambien en python 3 se puede hacer super()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set correct position
        # This has to be done because the bullet's rect is not based on an image
        self.rect = pygame.Rect(0,0, 
                                ai_settings.bullet_width, 
                                ai_settings.bullet_height) 
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as decimal value 
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color 
        self.speed_factor = ai_settings.bullet_speed_factor

    
    def update(self,):
        """Move the bullet up the screen"""
        # update the decimal position of the bullet
        self.y -= self.speed_factor # Tiene que ser negativo 
        self.rect.centery = self.y

    
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    