
import sys 
import time
import pygame 
from pygame.sprite import Group

from ship import Ship
from bullet import Bullet

# from alien import Alien
from alien import Alien
from alien_fleet import AlienFleet 


from settings import Settings
from game_stats import GameStats

from button import Button

class Game():

    def __init__(self):        
        # pygame initialization 
        pygame.init()
        # pygame.display_set_caption("Alien Invasion")        
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(( self.settings.screen_width, 
                                                self.settings.screen_height))
        self.stats = GameStats(self.settings)
        self.game_state = False

        # Entities
        # Ship  
        self.ship = Ship(self.settings, self.screen)
        # Alien Fleet 
        self.fleet = AlienFleet(self.settings, self.screen)
        # Bullets 
        self.bullets = Group()

        # UI 
        self.play_button = Button(self.screen, "Play")

    def run(self):

        while True:
            if self.stats.ship_left <= 0:
                self.game_state=False

            dt = self.clock.tick(60)/1000.0 # delta time 
            dt = min(dt, 0.1)
            # Check events 
            self.__check_events()
            # 
            if self.game_state:
                self.__check_if_reset()
                self.__update_bullets(dt)
                self.ship.update(dt)
                self.fleet.update(dt)

                self.__destroy_group_on_collision(self.bullets,self.fleet.alien_group)
            else:
                # pygame.mouse.set_visible(True)
                pass

            self.__update_screen()

    # RENDER
    def __update_screen(self):
        """Update images on the screen and double buffering"""
        self.screen.fill(self.settings.screen_color)

        # Draw bullets 
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw ship
        self.ship.blitme()

        # Draw each alien 
        for alien in self.fleet.alien_group:
            alien.blitme()

        if not self.game_state:
            self.play_button.draw_button()

        # Double buffering 
        pygame.display.flip()

    # RESET 
    def __check_if_reset(self):
        if(pygame.sprite.spritecollideany(self.ship, self.fleet.alien_group)):
            self.__reset_game()
        if(self.__check_if_screen_botton_hit()):
            self.__reset_game()
        if not self.fleet.alien_group:
            self.fleet.init_fleet()
            self.bullets.empty()
            # Speedup the level 
            self.settings.increase_speed()
    
    def __reset_game(self):
        # decrease the ship left 
        self.stats.ship_left -=1 
        # reset ship 
        self.ship.center_ship()
        # reset bullets 
        self.bullets.empty()
        # reset fleet 
        self.fleet.alien_group.empty()
        self.fleet.init_fleet()
        # delay 
        time.sleep(0.5)
        # 
        self.clock.tick()

    # UPDATES 
    def __update_bullets(self, deltaTime):
        for bullet in self.bullets.copy():
            self.bullets.update(deltaTime)
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet)

    # CHECK COLLISIONS 
    def __destroy_group_on_collision(self,g_1, g_2):
        collisions = pygame.sprite.groupcollide(g_1, g_2, True, True)

    def __check_if_screen_botton_hit(self):
        for alien in self.fleet.alien_group:
            if alien.rect.bottom >= self.settings.screen_height:
                return True 
        return False

    # EVENTS 
    def __check_events(self):
        """Respond to keypressed and mouse events"""
        for event in pygame.event.get(): # pygame.event.get() returns a list of events 
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.__check_key_down_evt(event)
            elif event.type == pygame.KEYUP:
                self.__check_keyup_events(event) 
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = pygame.mouse.get_pos()
                self.__check_mouse_events(event, mouse_pos)

    def __check_key_down_evt(self, event):
        """Respond to KEYDOWN events"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.__fire_bullet()            

    def __check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_a:
            self.ship.moving_left = False

    def __check_mouse_events(self, event, mouse_pos):
        if(self.play_button.check_if_pressed(mouse_pos)):
            button_clicked = self.play_button.rect.collidepoint(mouse_pos)
            if button_clicked and not self.game_state:                    
                self.stats.rest_stats()
                self.game_state= True;

                # Get rid of any remaining bullets and aliens 
                self.bullets.empty()
                self.fleet.alien_group.empty()

                self.fleet.init_fleet()
                self.ship.center_ship()

                # Reset dynamic settings 
                self.settings.initialize_dynamic_settings()

                pygame.mouse.set_visible(False)




    def __fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.settings, self.screen, self.ship)
            self.bullets.add(new_bullet)
    
