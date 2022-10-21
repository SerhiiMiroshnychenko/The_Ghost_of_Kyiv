import pygame


class Ship:
    """Клас для керування кораблем."""

    def __init__(self, ai_game):
        """Ініціалізувати корабель та задати його початкову позицію."""
        self.screen = ai_game.screen  # Зберігаємо екран як атрибут Ship.
        self.settings = ai_game.settings  # Налаштування корабля.
        self.screen_rect = ai_game.screen.get_rect()  # Отримуємо атрибут екрана
        # rect за допомогою методу get_rect та зберігаємо його в self.screen_rect.

        # Завантажити зображення корабля та отримати його rect.
        self.image = pygame.image.load('images/ua_ship.bmp')  # Завантажуємо зображення корабля
        self.rect = self.image.get_rect()  # Отримуємо доступ до атрибута rect
        # поверхні self.image, який знадобиться нам для позиціювання корабля.

        # Створювати кожен новий корабель внизу екрана, по центру.
        self.rect.midbottom = self.screen_rect.midbottom

        # Зберегти десяткове значення для позиції корабля по горизонталі.
        self.x = float(self.rect.x)

        # Індикатори руху.
        self.moving_right = False  # вправо
        self.moving_left = False   # вліво

    def update(self):
        """Оновити поточну позицію корабля на основі індикаторів руху."""
        if self.moving_right:  # Індикатор руху вправо.
            self.x += self.settings.ship_speed   # Зміщення позиції корабля по горизонталі вправо
            # на ship_speed пікселей. (Перемістити корабель праворуч.)
        if self.moving_left:   # Індикатор руху вліво.
            self.x -= self.settings.ship_speed   # Зміщення позиції корабля по горизонталі вліво
            # на ship_speed пікселей. (Перемістити корабель ліворуч.)

        # Оновити об'єкт rect з self.x.
        self.rect.x = self.x


    def blitme(self):
        """Намалювати корабель у його поточному розташуванні."""
        self.screen.blit(self.image, self.rect)  #
