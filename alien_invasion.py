import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Створює вікно, у якому будуть показуватися графічні елементи забавки.
        # Аргумент (self.settings.screen_width, self.settings.screen_height) - це кортеж, що позначає розміри вікна
        # завширшки та заввишки в пікселях.
        # Це "поверхня" (surface) - частина екрана, де показується елемент гри.
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # Створюємо корабель.

    def run_game(self):
        """Розпочати головний цикл гри."""
        while True:
            self._check_events()   # Перевіряємо нові події.
            self.ship.update()     # Оновлюємо поточну позицію корабля на основі індикатора руху.
            self._update_screen()  # Оновлюємо екран.

    def _check_events(self):
        # Слідкувати за подіями миші та клавіатури.
        for event in pygame.event.get():  # Змінна event - це якась дія гравця. Цей цикл for - це диспетчер подій,
            # що сприймає події та виконує відповідні дії. Функція pygame.event.get() повертає список подій, що
            # сталися після її останнього виклику.
            if event.type == pygame.QUIT:  # Якщо гравець зачиняє вікно:
                sys.exit()  # Вихід з гри.
            elif event.type == pygame.KEYDOWN:   # Якщо клавіша натиснута.
                if event.key == pygame.K_RIGHT:  # Якщо це клавіша "в право".
                    self.ship.moving_right = True  # Індикатор руху вправо => True
                    # self.ship.rect.x += 1  # Перемістити корабель праворуч.
            elif event.type == pygame.KEYUP:  # Коли клавіша відпускається.
                if event.key == pygame.K_RIGHT:  # Якщо це клавіша "в право".
                    self.ship.moving_right = False  # Індикатор руху вправо => False

    def _update_screen(self):
        # Наново перемалювати екран на кожній ітерації циклу.
        self.screen.fill(self.settings.bg_color)  # Малюємо фон
        self.ship.blitme()  # Малюємо корабель

        # Показати останній намальований екран.
        pygame.display.flip()


if __name__ == '__main__':
    # Створити екземпляр гри та запустити гру.
    ai = AlienInvasion()
    ai.run_game()
