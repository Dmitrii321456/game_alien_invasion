class Settings():
    """Класс для сохранения настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализируем настройки игры."""
        # Параметры экрана
        self.screen_width = 1400
        self.screen_height = 900
        self.bg_color = (120, 219, 226)
        self.ship_speed_factor = 1.5
        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
