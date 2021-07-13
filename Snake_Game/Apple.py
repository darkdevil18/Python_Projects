import pygame
from random import randint
from pygame.sprite import Sprite


class Apple(Sprite):
    """
    A class to draw apples randomly on the screen.
    """

    def __init__(self, ai_game):
        super().__init__()
        self.window = ai_game.window
        self.setting = ai_game.setting
        self.image = self.setting.apple_img
        self.x = 80
        self.y = 80

        self.rect = self.image.get_rect()

    def move_apple(self):
        self.x = randint(1, 29) * self.rect.width
        self.y = randint(1, 14) * self.rect.height

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
        pygame.display.flip()
