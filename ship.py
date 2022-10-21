import pygame


class Ship:
    """Клас для керування кораблем."""

    def __init__(self, ai_game):
        """Ініціалізувати корабель та задати його початкову позицію."""
        self.screen = ai_game.screen  # Зберігаємо екран як атрибут Ship.
        self.screen_rect = ai_game.screen.get_rect()  # Отримуємо атрибут екрана
        # rect за допомогою методу get_rect та зберігаємо його в self.screen_rect.

        # Завантажити зображення корабля та отримати його rect.
        self.image = pygame.image.load('images/ua_ship.bmp')  # Завантажуємо зображення корабля
        self.rect = self.image.get_rect()  # Отримуємо доступ до атрибута rect
        # поверхні self.image, який знадобиться нам для позиціювання корабля.

        # Створювати кожен новий корабель внизу екрана, по центру.
        self.rect.midbottom = self.screen_rect.midbottom

        # Індикатор руху.
        self.moving_right = False

    def update(self):

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні."""
        self.screen.blit(self.image, self.rect)  #
