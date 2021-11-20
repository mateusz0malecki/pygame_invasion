class GameStats:
    '''In-game statistics monitoring.'''

    def __init__(self, ai_game):
        '''Initialization of statistical data.'''
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        # The best score in the game.
        with open('high_score.txt') as file:
            self.high_score = float(file.read())

    def reset_stats(self):
        '''Initialization of statistical data that may change during the game.'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
