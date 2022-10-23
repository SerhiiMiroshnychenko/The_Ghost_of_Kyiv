import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet, Rocket


class AlienInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Перехід у повноекранний режим
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Створює вікно, у якому будуть показуватися графічні елементи забавки.
        # Аргумент (self.settings.screen_width, self.settings.screen_height) - це кортеж, що позначає розміри вікна
        # завширшки та заввишки в пікселях.
        # Це "поверхня" (surface) - частина екрана, де показується елемент гри.
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # Створюємо корабель.
        self.bullets = pygame.sprite.Group()  # Група, що зберігає всі "живі" кулі.
        self.rockets = pygame.sprite.Group()  # Група, що зберігає всі "живі" ракети.

    def run_game(self):
        """Розпочати головний цикл гри."""
        while True:
            self._check_events()   # Перевіряємо нові події.
            self.ship.update()     # Оновлюємо поточну позицію корабля на основі індикатора руху.
            self.bullets.update()  # Викликає bullet.update() для кожної кулі з групи bullets.
            self.rockets.update()  # Викликає rocket.update() для кожної ракети з групи rockets.

            # Позбавитися куль, що зникли.
            for bullet in self.bullets.copy():    # Для куль в копії групи bullets:
                if bullet.rect.bottom <= 0:       # Якщо rect низу(bottom) кулі менше як 0 (поза верхом екрана)
                    self.bullets.remove(bullet)   # Видалити ця кулю з групи.

            # Позбавитися ракет, що зникли.
            for rocket in self.rockets.copy():  # Для ракет в копії групи rockets:
                if rocket.rect.bottom <= 0:  # Якщо rect низу(bottom) ракети менше як 0 (поза верхом екрана)
                    self.rockets.remove(rocket)  # Видалити ця ракету з групи.

            self._update_screen()  # Оновлюємо екран.

    def _check_events(self):
        # Слідкувати за подіями миші та клавіатури.
        for event in pygame.event.get():  # Змінна event - це якась дія гравця. Цей цикл for - це диспетчер подій,
            # що сприймає події та виконує відповідні дії. Функція pygame.event.get() повертає список подій, що
            # сталися після її останнього виклику.
            if event.type == pygame.QUIT:  # Якщо гравець зачиняє вікно:
                sys.exit()  # Вихід з гри.
            elif event.type == pygame.KEYDOWN:   # Якщо клавіша натиснута.
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # Коли клавіша відпускається.
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагувати на натискання клавіш."""
        if event.key == pygame.K_RIGHT:  # Якщо це клавіша "в право".
            self.ship.moving_right = True  # Індикатор руху вправо => True
        elif event.key == pygame.K_LEFT:  # Якщо це клавіша "вліво".
            self.ship.moving_left = True  # Індикатор руху вліво => True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_r:
            self._fire_rocket()

    def _check_keyup_events(self, event):
        """Реагувати, коли клавіша не натиснута."""
        if event.key == pygame.K_RIGHT:  # Якщо це клавіша "в право".
            self.ship.moving_right = False  # Індикатор руху вправо => False
        elif event.key == pygame.K_LEFT:  # Якщо це клавіша "вліво".
            self.ship.moving_left = False  # Індикатор руху вліво => False

    def _fire_bullet(self):
        """Створити нову кулю та додати її до групи куль."""
        new_bullet = Bullet(self)     # Створюємо нову кулю.
        self.bullets.add(new_bullet)  # Додаємо її до групи bullets з допомогою методу add.

    def _fire_rocket(self):
        """Створити нову ракету та додати її до групи ракет."""
        new_rocket = Rocket(self)     # Створюємо нову ракету.
        self.rockets.add(new_rocket)  # Додаємо її до групи rockets з допомогою методу add.

    def _update_screen(self):
        # Наново перемалювати екран на кожній ітерації циклу.
        self.screen.fill(self.settings.bg_color)  # Малюємо фон
        self.ship.blitme()  # Малюємо корабель
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for rocket in self.rockets.sprites():
            rocket.draw_rocket()

        # Показати останній намальований екран.
        pygame.display.flip()


if __name__ == '__main__':
    # Створити екземпляр гри та запустити гру.
    ai = AlienInvasion()
    ai.run_game()
