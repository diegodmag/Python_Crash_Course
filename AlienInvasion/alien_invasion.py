import pygame

# Importing settings 
from settings import Settings

# Import ships 
from ship import Ship

# Import alien ships 
from alien_fleet import AlienFleet

# Import game functions 
import game_functions as gf

from game_stats import GameStats

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

    screen = pygame.display.set_mode((ai_settings.screen_width, 
                                      ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)

    # Make a ship 
    ship = Ship(ai_settings,screen)

    # Make an aline // Working 
    fleet = AlienFleet(ai_settings, screen)

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

        # NEEDS: to be abstracted into game_functions 
        if not fleet.alien_group:
            fleet.init_fleet()
            bullets.empty()
        # NEEDS: to be abstracted into game_functions 
        if pygame.sprite.spritecollideany(ship, fleet.alien_group):
            gf.on_ship_hit(ai_settings, ship, bullets, fleet)

        gf.update_bullets(bullets, dt)
        
        ship.update(dt)

        fleet.update(dt)

        gf.destroy_group_on_collision(bullets, fleet.alien_group)

        gf.update_screen(ai_settings, screen, ship, bullets, fleet)

run_game()