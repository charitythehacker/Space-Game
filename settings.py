
class Settings:
    """A class to store the settings of alien invasion game"""
    def __init__(self):
        """Initializes the static games settings."""
        self.screen_width = 1200
        self.screen_height= 800
        self.bg_color = (0,0,0)

        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color= (77,77, 255)
        self.bullets_allowed= 3

        #alien settings
        self.fleet_drop_speed = 10
        #fleet direction of 1 reps right; -1 reps left
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.bullet_speed= 2.5
        self.alien_speed = 1.0
        self.alien_points = 50
        #fleet direction of 1 reps right, -1 reps left
        self.fleet_direction =1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale 
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= int(self.score_scale)
        print(self.alien_points)
