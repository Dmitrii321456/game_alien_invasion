import pygame


class Ship():

    def __init__(self, screen) -> None:
        """Инициализируем корабль и создаем его изначальную позицию"""
        self.screen = screen

        # Загрузка изображения корабля и получения прямоугольника
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабля появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновление позиции корабля с учетом флага"""
        if self.moving_right:
            self.rect.centerx += 1

        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Рисуем корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
