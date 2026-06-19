import sys
import pygame

# Importing settings 
from settings import Settings

# Import ships 
from ship import Ship

def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    # Initialize settings 
    ai_settings = Settings()

    # The screen is called a Surface , each element displayed is a surface
    # This surface is re-drawn on every pass 
    screen = pygame.display.set_mode((ai_settings.screen_width, 
                                      ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # Make a ship 
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Redraw the screen during each pass through the loop 
        screen.fill(ai_settings.screen_color)
        ship.blitme()
        # Make the most recently drawn screen visible.
        # This is the double buffering 
        pygame.display.flip()

run_game()