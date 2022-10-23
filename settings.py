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
        self.bullet_speed = 0.8
        # Налаштування для ракети
        self.rocket_speed = 0.5
