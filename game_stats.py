class GameStats:
    """Відстежування статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізація статистики."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Розпочати гру в активному стані
        self.game_active = True

    def reset_stats(self):
        """Ініціалізація статистики, що може змінюватися впродовж гри."""
        self.ship_left = self.settings.ship_limit  # Скільки кораблів залишилося
