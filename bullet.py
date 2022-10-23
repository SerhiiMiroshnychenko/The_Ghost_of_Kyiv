import pygame
from pygame.sprite import Sprite
from random import choice


class Bullet(Sprite):
    """Клас для керування кулями, випущеними з корабля."""

    def __init__(self, ai_game):  # ai_game - поточний екземпляр гри, як аргумент
        """Створити новий об'єкт bullet у поточній позиції корабля."""
        super().__init__()  # Викликаємо успадкування від класу Sprite
        self.screen = ai_game.screen       # Додаємо атрибути для об'єкта screen
        self.settings = ai_game.settings   # Додаємо атрибути для об'єкта settings

        # Завантажити зображення кулі та отримати її rect.
        self.image_0 = pygame.image.load('images/bullet_0.bmp')
        self.image_1 = pygame.image.load('images/bullet_1.bmp')
        self.image_2 = pygame.image.load('images/bullet_2.bmp')
        self.rect = self.image_0.get_rect()  # Отримуємо доступ до атрибута rect
        # поверхні self.image, який знадобиться нам для позиціювання кулі.

        self.rect.midtop = ai_game.ship.rect.midtop  # Прирівнюємо координати верху середини кулі
        # до верхівки середини корабля.

        # Зберегти позицію кулі як десяткове значення.
        self.y = float(self.rect.y)

    def update(self):
        """Посунути куля нагору екраном."""
        # Оновити десяткову позицію кулі.
        self.y -= self.settings.bullet_speed  # Зменшуємо координату кулі == вона просувається вгору.
        # Оновити позицію rect.
        self.rect.y = self.y

    def draw_bullet(self):
        """Намалювати кулю на екрані."""
        self.screen.blit(choice([self.image_0, self.image_1, self.image_2]), self.rect)


class Rocket(Bullet):
    """Клас для керування ракетами, випущеними з корабля."""
    def __init__(self, ai_game):  # ai_game - поточний екземпляр гри, як аргумент
        """Створити новий об'єкт bullet у поточній позиції корабля."""
        super().__init__()  # Викликаємо успадкування від класу Bullet
        self.screen = ai_game.screen  # Додаємо атрибути для об'єкта screen
        self.settings = ai_game.settings  # Додаємо атрибути для об'єкта settings

        # Завантажити зображення ракети та отримати її rect.
        self.image_0 = pygame.image.load('images/rocket0.bmp')
        self.image_1 = pygame.image.load('images/rocket1.bmp')
        self.image_2 = pygame.image.load('images/rocket2.bmp')
        self.image_3 = pygame.image.load('images/rocket3.bmp')
        self.image_4 = pygame.image.load('images/rocket4.bmp')
        self.rect = self.image_0.get_rect()  # Отримуємо доступ до атрибута rect
        # поверхні self.image, який знадобиться нам для позиціювання ракети.

    def draw_rocket(self):
        """Намалювати кулю на екрані."""
        self.screen.blit(choice([self.image_0, self.image_1, self.image_2, self.image_3, self.image_4]), self.rect)
