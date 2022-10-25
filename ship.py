import pygame
from random import choice


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
        self.image1 = pygame.image.load('images/ua_ship_1.bmp')
        self.image2 = pygame.image.load('images/ua_ship_2.bmp')
        self.image3 = pygame.image.load('images/ua_ship_3.bmp')
        self.image4 = pygame.image.load('images/ua_ship_4.bmp')
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
        if self.moving_right and self.rect.right < self.screen_rect.right:  # Індикатор руху вправо.
            # self.rect.right < self.screen_rect.right - перевірка чи не дійшов краю екрана
            self.x += self.settings.ship_speed   # Зміщення позиції корабля по горизонталі вправо
            # на ship_speed пікселей. (Перемістити корабель праворуч.)
        if self.moving_left and self.rect.left > 0:   # Індикатор руху вліво.
            # self.rect.left > 0 - перевірка чи не дійшов краю екрана
            self.x -= self.settings.ship_speed   # Зміщення позиції корабля по горизонталі вліво
            # на ship_speed пікселей. (Перемістити корабель ліворуч.)

        # Оновити об'єкт rect з self.x.
        self.rect.x = self.x

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні."""
        self.screen.blit(choice([self.image, self.image1, self.image2, self.image3, self.image4]), self.rect)  #

    def center_ship(self):
        """Відцентрувати корабель на екрані."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

