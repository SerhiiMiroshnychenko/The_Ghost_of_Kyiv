import sys

import pygame


class AlienInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))  # Створює вікно, у якому будуть показуватися графічні
        # елементи забавки. Аргумент (1200, 800) - це кортеж, що позначає розміри вікна завширшки та заввишки
        # в пікселях. Це "поверхня" (surface) - частина екрана, де показується елемент гри.
        pygame.display.set_caption("Alien Invasion")

        # Задати колір фону
        self.bg_color = (100, 100, 120)  # red-green-blue

    def run_game(self):
        """Розпочати головний цикл гри."""
        while True:
            # Слідкувати за подіями миші та клавіатури.
            for event in pygame.event.get():  # Змінна event - це якась дія гравця. Цей цикл for - це диспетчер подій,
                # що сприймає події та виконує відповідні дії. Функція pygame.event.get() повертає список подій, що
                # сталися після її останнього виклику.
                if event.type == pygame.QUIT:  # Якщо гравець зачиняє вікно:
                    sys.exit()                 # Вихід з гри.

            # Наново перемалювати екран на кожній ітерації циклу.
            self.screen.fill(self.bg_color)

            # Показати останній намальований екран.
            pygame.display.flip()


if __name__ == '__main__':
    # Створити екземпляр гри та запустити гру.
    ai = AlienInvasion()
    ai.run_game()
