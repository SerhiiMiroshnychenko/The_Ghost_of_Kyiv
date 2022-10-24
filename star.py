import pygame
from pygame.sprite import Sprite
from random import choice


class Star(Sprite):
    """Клас для генерування зірок."""
    def __init__(self, ai_game):
        """Ініціалізувати зірку і додати її розташування."""
        super().__init__()
        self.screen = ai_game.screen  # Додаємо атрибути для об'єкта screen
        self.settings = ai_game.settings  # Додаємо атрибути для об'єкта settings
        self.color = self.settings.star_color

        # Створити rect зірки у (0, 0) та задати правильну позицію.
        self.rect = pygame.Rect(0, 0, self.settings.star_width, self.settings.star_height)
        x_position = choice(range(self.settings.screen_width))
        y_position = choice(range(self.settings.screen_higth))
        self.rect.x = x_position
        self.rect.y = y_position

    def draw_star(self):
        """Намалювати зірку на екрані."""
        pygame.draw.rect(self.screen, self.color, self.rect)
