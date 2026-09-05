import pygame 

from alien import Alien 

class AlienFleet():

    def __init__(self, ai_settings, screen):

        self.ai_settings = ai_settings
        self.screen = screen 
        self.alien_group = pygame.sprite.Group()

        self.init_fleet()

    def init_fleet(self):
        # Determine the spacing
        # Spacing between aliens is one width and height 
        alien_model = Alien(self.ai_settings,self.screen) # Just for measurements 
        alien_width, alien_height =  alien_model.rect.size # get dimentions 

        screen_width, screen_height = self.screen.get_size() 

        spacing_x = alien_width*2

        current_x, current_y = alien_width, alien_height

        #Column creation 
        while current_y < screen_height - alien_height*3:
            # Row creation 
            while current_x < (screen_width-alien_width):
                self.create_alien(current_x, current_y);            
                current_x += spacing_x
            current_x = alien_width
            current_y+=alien_height*2

    def create_alien(self,x_pos, y_pos):
        new_alien = Alien(self.ai_settings, self.screen) 
        # new_alien.center = x_pos
        new_alien.x = x_pos 
        new_alien.rect.x = x_pos
        new_alien.rect.y = y_pos
        self.alien_group.add(new_alien)

    def update(self, deltaTime):

        self.check_fleet_edges(deltaTime)

        for alien in self.alien_group:
            alien.update(deltaTime)

    def check_fleet_edges(self, deltaTime):
        for alien in self.alien_group:
            if alien.check_edges():
                # change direction 
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        # Drop the entire fleet 
        for alien in self.alien_group:
            alien.rect.y += self.ai_settings.fleet_drop_speed 
        self.ai_settings.fleet_direction *= -1
