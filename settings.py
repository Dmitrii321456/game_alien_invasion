class Settings():
    """Класс для сохранения настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализируем настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 500
        self.bg_color = (120, 219, 226)
        self.ship_speed_factor = 1.5
