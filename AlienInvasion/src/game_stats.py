
class GameStats():

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.settings = ai_settings 
        self.ship_left = self.settings.ship_limit 

    def rest_stats(self):
        # self.ship_left - self.settings.ship_limit
        self.ship_left = self.settings.ship_limit 