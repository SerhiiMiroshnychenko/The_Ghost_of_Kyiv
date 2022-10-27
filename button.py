import pygame.font  # Модуль font дозволяє показувати текст на екрані

from settings import Settings


class Button:

    def __init__(self, ai_game, msg):  # параметр msg містить текст
        """Ініціалізація атрибутів кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Задати розміри та властивості кнопки
        self.wight, self.height = 300, 50  # Розміри кнопки
        self.button_color = (100, 100, 150)    # Колір кнопки
        self.text_color = (200, 200, 250)  # Колір тексту
        self.font = pygame.font.SysFont(None, 48)  # Визначаємо атрибут font (текст):
        # None -> повернення до уставної гарнітури, 48 -> розмір тексту

        # Створити об'єкт rect кнопки та відцентрувати його
        self.rect = pygame.Rect(0, 0, self.wight, self.height)  # Створюємо rect кнопки з її розмірами в 0,0
        self.rect.center = self.screen_rect.center  # center -> розташування в центрі екрана

        # Повідомлення на кнопці треба показати лише один раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Перетворити текст на зображення та розмістити по центру кнопки"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)  # Перетворити текст
        # на зображення. True -> умикнути згладжування країв картинки
        self.msg_image_rect = self.msg_image.get_rect()  # Створюємо rect на базі зображення
        self.msg_image_rect.center = self.rect.center    # Прирівняємо центри кнопки та тексту

    def draw_button(self):
        # Намалювати порожню кнопку, а тоді -- повідомлення
        self.screen.fill(self.button_color, self.rect)  # Створюємо прямокутну частину кнопки
        self.screen.blit(self.msg_image, self.msg_image_rect)  # Малюємо зображення тексту на екрані


class Greeting(Button):
    def __init__(self, ai_game, msg):  # параметр msg містить текст
        """Ініціалізація атрибутів кнопки"""
        super().__init__(ai_game, msg)
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Задати розміри та властивості кнопки
        self.wight, self.height = 750, 50  # Розміри кнопки
        self.button_color = (220, 160, 0)    # Колір кнопки
        self.text_color = (0, 100, 180)  # Колір тексту
        self.font = pygame.font.SysFont(None, 48)  # Визначаємо атрибут font (текст):
        # None -> повернення до уставної гарнітури, 48 -> розмір тексту

        # Створити об'єкт rect кнопки та відцентрувати його
        self.rect = pygame.Rect(0, 0, self.wight, self.height)
        self.rect.center = (self.screen_rect.width / 2, 200)

        # Повідомлення на кнопці треба показати лише один раз
        self._prep_msg(msg)


