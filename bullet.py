import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Клас для керування кулями, випущеними з корабля."""

    def __init__(self, ai_game):  # ai_game - поточний екземпляр гри, як аргумент
        """Створити новий об'єкт bullet у поточній позиції корабля."""
        super().__init__()  # Викликаємо успадкування від класу Sprite
        self.screen = ai_game.screen       # Додаємо атрибути для об'єкта screen
        self.settings = ai_game.settings   # Додаємо атрибути для об'єкта settings
        self.color = self.settings.bullet_color

        # Створити rect кулі у (0, 0) та задати правильну позицію.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
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
        pygame.draw.rect(self.screen, self.color, self.rect)
