import pygame


class Ship():

    def __init__(self, screen, ai_settings) -> None:
        """Инициализируем корабль и создаем его изначальную позицию"""
        self.screen = screen
        self.air_settings = ai_settings

        # Загрузка изображения корабля и получения прямоугольника
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабля появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Обновление позиции корабля с учетом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.air_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.air_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.air_settings.ship_speed_factor

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.air_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Рисуем корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
