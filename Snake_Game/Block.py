from pygame.sprite import Sprite

from settings import *


class Block(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.setting = Setting()
        self.length = 1
        self.direction = 'right'
        self.window = ai_game.window
        self.x = [40] * self.length
        self.y = [40] * self.length
        self.image = self.setting.block_img

        self.rect = self.image.get_rect()

    def draw(self):
        """
        Draws the snake on the screen
        """
        # self.window.fill(self.setting.bg_color)
        self.window.blit(self.setting.bg_img, self.window.get_rect())
        for i in range(self.length):
            self.window.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        if self.direction != 'down':
            self.direction = 'up'

    def move_down(self):
        if self.direction != 'up':
            self.direction = 'down'

    def move_right(self):
        if self.direction != 'left':
            self.direction = 'right'

    def move_left(self):
        if self.direction != 'right':
            self.direction = 'left'

    def move(self) -> None:
        """
        Controls the movement of the snake
        :return: None
        """
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'right':
            self.x[0] += 40
        if self.direction == 'left':
            self.x[0] -= 40
        if self.direction == 'up':
            self.y[0] -= 40
        if self.direction == 'down':
            self.y[0] += 40
        window_rect = self.window.get_rect()
        if self.x[0] < window_rect.left:
            self.x[0] += window_rect.width
        if self.x[0] > window_rect.right:
            self.x[0] = window_rect.left
        if self.y[0] < window_rect.top:
            self.y[0] += window_rect.height
        if self.y[0] > window_rect.bottom:
            self.y[0] = window_rect.top

        self.draw()

    def _increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
