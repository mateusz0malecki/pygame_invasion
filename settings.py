class Settings:
    '''Class designed to store all game settings.'''

    def __init__(self):
        '''Initializing the game settings.'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship related settings.
        self.ship_limit = 3

        # Bullet related settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 3

        # Alien related settings
        self.fleet_drop_speed = 50

        # Changing speed of the game
        self.speedup_scale = 1.2

        # Changing amount of points gained by hitting an alien
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Settings that change values during gameplay.'''
        self.alien_speed = 0.1
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_points = 50

        # A fleet_direction value of 1 means moving right, and -1 left.
        self.fleet_direction = 1

    def increase_speed(self):
        '''Change the game speed settings.'''
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
