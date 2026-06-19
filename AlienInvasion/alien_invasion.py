import pygame

# Importing settings 
from settings import Settings

# Import ships 
from ship import Ship

# Import game functions 
import game_functions as gf

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
    ship = Ship(ai_settings,screen)

    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

run_game()