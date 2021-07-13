import pygame


class Setting:
    def __init__(self):
        self.bg_color = (115, 115, 5)
        self.text_color = (175, 201, 28)
        self.block_img = pygame.image.load("resources/block.jpg").convert()
        self.apple_img = pygame.image.load("resources/apple.png")
        self.bg_img = pygame.image.load("resources/background.jpg").convert()
