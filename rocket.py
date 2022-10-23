import pygame
from random import choice
from bullet import Bullet


class Rocket(Bullet):
    """Клас для керування ракетами, випущеними з корабля."""
    def __init__(self, ai_game):  # ai_game - поточний екземпляр гри, як аргумент
        """Створити новий об'єкт bullet у поточній позиції корабля."""
        super().__init__(ai_game)  # Викликаємо успадкування від класу Bullet
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

        self.rect.midtop = ai_game.ship.rect.midtop  # Прирівнюємо координати верху середини ракети
        # до верхівки середини корабля.

        # Зберегти позицію ракети як десяткове значення.
        self.y = float(self.rect.y)

    def update(self):
        """Посунути ракету нагору екраном."""
        # Оновити десяткову позицію ракети.
        self.y -= self.settings.rocket_speed  # Зменшуємо координату ракети == вона просувається вгору.
        # Оновити позицію rect.
        self.rect.y = self.y

    def draw_rocket(self):
        """Намалювати кулю на екрані."""
        self.screen.blit(choice([self.image_0, self.image_1, self.image_2, self.image_3, self.image_4]), self.rect)
