class GameStats:
    """Відстежування статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізація статистики."""
        self.settings = ai_game.settings
        self.reset_stats()

