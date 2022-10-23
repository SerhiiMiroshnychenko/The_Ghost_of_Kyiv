class Settings:
    """Клас для збереження всіх налаштувань гри."""

    def __init__(self):
        """Ініціалізувати налаштування гри."""
        # Screen settings
        self.screen_width = 1200  # Ширина вікна
        self.screen_height = 750  # Висота вікна
        self.bg_color = (100, 100, 120)  # Колір фона (red-green-blue)
        # Налаштування корабля
        self.ship_speed = 1.1
        # Налаштування для кулі
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 180, 180)
        self.bullet_allowed = 3
        # Налаштування для ракети
        self.rocket_speed = 0.1
        self.rocket_allowed = 5
