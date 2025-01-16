
class GameStats:
    """Track game stats"""

    def __init__(self, ai_game):
        
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0


    def reset_stats(self):
        """Init stats taht can change during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0