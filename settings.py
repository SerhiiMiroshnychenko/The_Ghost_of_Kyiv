class Settings:
    """Клас для збереження всіх налаштувань гри."""

    def __init__(self):
        """Ініціалізувати налаштування гри."""
        # Screen settings
        self.screen_width = 1200  # Ширина вікна
        self.screen_height = 750  # Висота вікна
        self.bg_color = (50, 50, 70)  # Колір фона (red-green-blue)
        # Налаштування корабля
        self.ship_speed = 1.1
        # Налаштування для кулі
        self.bullet_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (180, 50, 0)
        self.bullet_allowed = 3
        # Налаштування для ракети
        self.rocket_speed = 0.1
        self.rocket_allowed = 5
        # Налаштування для зірки
        self.star_width = 3
        self.star_height = 12
        self.star_color = (200, 200, 250)
        # Налаштування прибульця
        self.alien_speed = 1.0      # Швидкість руху прибульця вбік
        self.fleet_drop_speed = 10  # Швидкість спуску флоту
        # fleet_direction 1 означає напрямок руху праворуч; -1 -- ліворуч.
        self.fleet_direction = 1

