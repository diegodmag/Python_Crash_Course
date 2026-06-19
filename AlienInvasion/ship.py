import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings 

        """Load the screen and Image and get its rect"""
        # This function return a surface representing the ship 
        self.image = pygame.image.load('images/ship.bmp')
        
        # Access the surface rect attribute 
        self.rect = self.image.get_rect() # el rectangulo es el de la imagen 
        self.screen_rect = screen.get_rect() # el rectangulo de la imagen 

        
        """Start each new ship at the bottom center of the screen"""
        self.rect.centerx = self.screen_rect.centerx # The center of the rectangle is the same as the screen 
        self.rect.bottom = self.screen_rect.bottom  # The bottom of the rect is allign with the screen bottom
        
        # Store a decimal value for the ship's center 
        self.center = float(self.rect.left) # This is the cneter of the rect but as float

        # Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        """Draw the ship at its current location""" 
        self.screen.blit(self.image, self.rect)
        # Entonces para dibujar, se usa blit y requiere la imagen y el rectangulo
    
    def update(self):
        """Update the ship's position based on the movement flag"""         
        print(f"Position {self.rect.centerx}\n")
        # Update the ship's center value, not the rect 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx +=1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Beacuse centerx only stores int values, it will take only 
        # the integer part of self.center
        self.rect.centerx = self.center
