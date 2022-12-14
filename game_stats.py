import json


class GameStats:
    """Відстежування статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізація статистики."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Розпочати гру в активному стані
        self.game_active = False
        # Рекорд не анульовується
        try:
            with open("high_score.json") as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Ініціалізація статистики, що може змінюватися впродовж гри."""
        self.ship_left = self.settings.ship_limit  # Скільки кораблів залишилося
        self.score = 0  # Рахунок

