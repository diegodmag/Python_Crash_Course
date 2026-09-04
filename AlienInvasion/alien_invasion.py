import pygame

# Importing settings 
from settings import Settings

# Import ships 
from ship import Ship

# Import alien 
from alien import Alien

# Import game functions 
import game_functions as gf

# This works as a list 
from pygame.sprite import Group

# sys.prefix -> Una cadena que da el prefijo del sitio especifico donde los archivos 
# de python independientemente de la plataforma son instalados. En UNIX por defecto es 
# sys.prefix = /usr/local

# sys.exec_prefix -> Una cadena de caracteres que guarda el directiorio donde los archivos
# dependientes de plataforma de python son instalados. 


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

    # Make an aline // Working 
    aliens = []
    gf.create_fleet(ai_settings, screen, aliens)
    # Fill the aliens group

    # Mak a group to store bullets in 
    bullets= Group()

    # Init clock 
    clock = pygame.time.Clock(); 
    target_fps = 60

    # Start the main loop for the game.
    while True:

        dt = clock.tick(60) / 1000.0 # delta time in seconds 
    # Watch for keyboard and mouse e    vents.
        gf.check_events(ai_settings, screen, ship, bullets)
        # Because bullets is a Group of sprites, the update()
        # is run for every bullet 
        gf.update_bullets(bullets, dt)
        
        ship.update(dt)

        gf.update_aliens(aliens, dt) # working on this

        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()