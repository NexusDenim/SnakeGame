import config


class Player:
    _game_instance = None
    _screen_instance = None
    _player = None

    _X = None
    _Y = None
    player_speed = 0.1
    _max_speed = 10

    def __init__(self, game_instance, screen_instance, x=config.game_config['width'] / 2,
                 y=config.game_config['height'] / 2, logo=config.game_config['game_icon']):
        self._X = x
        self._Y = y
        player_logo = logo if logo != '' else config.game_config['game_icon']
        self._player = game_instance.image.load(player_logo)
        self._screen_instance = screen_instance
        self._game_instance = game_instance
        screen_instance.blit(self._player, (self._X, self._Y))
        game_instance.display.update()

    def get_position(self):
        return {'X': self._X, 'Y': self._Y}

    def set_position(self, x, y):
        self._X = x if x != '' else self._X
        self._Y = y if y != '' else self._Y
        return self.get_position()

    def set_x(self, x): self._X = x if config.game_config['width'] > x > 0 else self._X

    def set_y(self, y): self._Y = y if config.game_config['height'] > y > 0 else self._Y

    def set_player_speed(self, speed): self.player_speed = speed if speed < self._max_speed else self._max_speed

    def move_right(self):
        self.set_x(self._X + self.player_speed)
        self._screen_instance.blit(self._player, (self._X, self._Y))
        self._game_instance.display.update()

    def move_left(self):
        self.set_x(self._X - self.player_speed)
        self._screen_instance.blit(self._player, (self._X, self._Y))

    def move_up(self):
        self.set_y(self._Y - self.player_speed)
        self._screen_instance.blit(self._player, (self._X, self._Y))

    def move_down(self):
        self.set_y(self._Y + self.player_speed)
        self._screen_instance.blit(self._player, (self._X, self._Y))
