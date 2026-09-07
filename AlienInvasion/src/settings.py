class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230,230,230)

        
        # self.ship_speed_factor = 300 # this is now in pixels per second 
        self.ship_limit = 3 

        # Bullets settings 
        # self.bullet_speed_factor = 200
        self.bullet_width = 5
        self.bullet_height = 15 
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien settings 
        # How many alienst 
        self.aliens_ammount = 8
        # self.alien_speed = 100 
        self.fleet_drop_speed = 20
        # flet direction 
        # self.fleet_direction = 1

        # How quickly the game speeds up 
        self.speedup_scale = 1.25 
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings that change throughout the game"""
        self.ship_speed_factor = 200 
        self.bullet_speed_factor = 200
        self.alien_speed = 100
        # Fleet direction 
        self.fleet_direction =1
        pass

    def increase_speed(self):
        """Increase the speed limit"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed *= self.speedup_scale