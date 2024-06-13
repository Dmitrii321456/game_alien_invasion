import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Инициализируем игру и создаем объект экрана
    # Инициализируем pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Создание корабля
    ship = Ship(screen, ai_settings)
    # Создание группы для хранения пуль
    bullets = Group()
    # Создаем флот пришельцев
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)

    # Создание пришельца
    alien = Alien(ai_settings, screen)
    # Запуск основного цикла игры
    while True:
        # Отслеживаем событие клавиатуры и мыши.
        gf.check_events(ai_settings, screen,
                        ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


run_game()
