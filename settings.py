class Settings:
    """Клас для збереження всіх налаштувань гри."""

    def __init__(self):
        """Ініціалізувати налаштування гри."""
        # Screen settings
        self.screen_width = 1200  # Ширина вікна
        self.screen_height = 750  # Висота вікна
        self.bg_color = (100, 100, 120)  # Колір фона (red-green-blue)
        # Налаштування корабля
        self.ship_speed = 1.5
        # Налаштування для кулі
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
