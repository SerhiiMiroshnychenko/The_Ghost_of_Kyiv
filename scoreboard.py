import pygame.font


class Scoreboard:
    """Клас, що виводить рахунок"""

    def __init__(self, ai_game):
        """Ініціалізація атрибутів, пов'язаних із рахунком"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Налаштування шрифту для показу рахунку
        self.text_color = (250, 0, 0)  # Визначаємо колір тексту
        self.font = pygame.font.SysFont(None, 48)  # Робимо екземпляр об'єкта шрифту

        # Підготувати зображення з початковим рахунком
        self.prep_score()

    def prep_score(self):
        """Перетворити рахунок на зображення"""
        rounded_score = round(self.stats.score, -1)  # Округляємо рахунок до найближчого десятка
        score_str = "{:,}".format(rounded_score)  # Перетворюємо числове значення рахунку у стрічку
        # Передаємо стрічку функції render, що створює зображення. Передаємо render кольори екрану та тексту
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Показати рахунок у верхньому правому куті екрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # Правий край рахунку на 20 пікселів лівіше
        # правого краю екрану
        self.score_rect.top = 20  # Верхній край рахунку на 20 пікселів нижче за верхній край екрану

    def show_score(self):
        """Показати рахунок на екрані"""
        self.screen.blit(self.score_image, self.score_rect)

