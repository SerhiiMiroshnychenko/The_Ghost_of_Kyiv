import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from rocket import Rocket
from alien import Alien


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
        self.aliens = pygame.sprite.Group()   # Група, що зберігає всіх "живих" ворогів.

        self._create_fleet()

    def run_game(self):
        """Розпочати головний цикл гри."""
        while True:
            self._check_events()    # Перевіряємо нові події.
            self.ship.update()      # Оновлюємо поточну позицію корабля на основі індикатора руху.
            self._update_bullets()  # Оновити позицію куль та позбавитися старих куль.
            self._update_rockets()  # Оновити позицію ракет та позбавитися старих ракет.
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
        if len(self.bullets) < self.settings.bullet_allowed:  # Якщо кількість куль на екрані менша за дозволену
            new_bullet = Bullet(self)     # Створюємо нову кулю.
            self.bullets.add(new_bullet)  # Додаємо її до групи bullets з допомогою методу add.

    def _fire_rocket(self):
        """Створити нову ракету та додати її до групи ракет."""
        if len(self.rockets) < self.settings.rocket_allowed:  # Якщо кількість ракет на екрані менша за дозволену
            new_rocket = Rocket(self)     # Створюємо нову ракету.
            self.rockets.add(new_rocket)  # Додаємо її до групи rockets з допомогою методу add.

    def _update_bullets(self):
        """Оновити позицію куль та позбавитися старих куль."""
        # Оновити позиції куль.
        self.bullets.update()  # Викликає bullet.update() для кожної кулі з групи bullets.

        # Позбавитися куль, що зникли.
        for bullet in self.bullets.copy():  # Для куль в копії групи bullets:
            if bullet.rect.bottom <= 0:  # Якщо rect низу(bottom) кулі менше як 0 (поза верхом екрана)
                self.bullets.remove(bullet)  # Видалити ця кулю з групи.

    def _update_rockets(self):
        """Оновити позицію ракет та позбавитися старих ракет."""
        # Оновити позицію ракет.
        self.rockets.update()  # Викликає rocket.update() для кожної ракети з групи rockets.

        # Позбавитися ракет, що зникли.
        for rocket in self.rockets.copy():  # Для ракет в копії групи rockets:
            if rocket.rect.bottom <= 0:  # Якщо rect низу(bottom) ракети менше як 0 (поза верхом екрана)
                self.rockets.remove(rocket)  # Видалити ця ракету з групи.

    def _create_fleet(self):
        """Створити флот чужинців."""
        # Створити прибульців та визначити кількість прибульців в ряду.
        # Відстань між прибульцями дорівнює ширині одного прибульця.
        alien = Alien(self)  # Перший чужий, що не стане частиною флоту. Потрібен для розрахунків.
        alien_width = alien.rect.width  # Отримуємо ширину прибульця з його атрибута rect.
        available_space_x = self.settings.screen_width - (2 * alien_width)  # Рахуємо скільки місця
        # є під прибульців по горизонталі.
        number_aliens_x = available_space_x // (2 * alien_width)  # Рахуємо скільки прибульців туди поміститься.

        # Створити перший ряд прибульців.
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        """Створити прибульця та поставити його до ряду."""
        alien = Alien(self)  # Створити прибульця та поставити його до ряду.
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number  # Координата кожного наступного прибульця по осі х
        alien.rect.x = alien.x  # Задаємо розташування rect прибульця.
        self.aliens.add(alien)  # Додаємо новоствореного чужого до групи aliens.

    def _update_screen(self):
        # Наново перемалювати екран на кожній ітерації циклу.
        self.screen.fill(self.settings.bg_color)  # Малюємо фон
        self.ship.blitme()  # Малюємо корабель
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for rocket in self.rockets.sprites():
            rocket.draw_rocket()
        self.aliens.draw(self.screen)

        # Показати останній намальований екран.
        pygame.display.flip()


if __name__ == '__main__':
    # Створити екземпляр гри та запустити гру.
    ai = AlienInvasion()
    ai.run_game()
