import time

from pygame.locals import *

from Apple import *
from Block import *
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1200, 600))
        self.setting = Setting()
        pygame.display.set_caption("BLOCKS AND APPLE")
        self.block = Block(self)
        self.block.draw()
        self.apple = Apple(self)
        self.apple.draw()
        self.score = self.block.length - 1

        self.window.blit(self.setting.bg_img, self.window.get_rect())
        pygame.display.flip()

    def _check_collision(self):
        """
        A function to check collision.
        """
        if self.block.x[0] >= self.apple.x and self.block.x[0] < self.apple.x + self.apple.rect.width:
            if self.block.y[0] >= self.apple.y and self.block.y[0] < self.apple.y + self.apple.rect.height:
                self.block._increase_length()
                self.show_score()
                self.apple.move_apple()
        for i in range(2, self.block.length):
            if self.block.x[0] >= self.block.x[i] and self.block.x[0] < self.block.x[i] + 40:
                if self.block.y[0] >= self.block.y[i] and self.block.y[0] < self.block.y[i] + 40:
                    raise "Collided Itself"

    def _check_keydown_events(self, key):
        """
        A function to check all the key_down events
        :parameter: key = event.key
        """
        if key == K_UP:
            self.block.move_up()
        if key == K_DOWN:
            self.block.move_down()
        if key == K_RIGHT:
            self.block.move_right()
        if key == K_LEFT:
            self.block.move_left()

    def play(self):
        self.block.move()
        self.apple.draw()
        self._check_collision()
        self.show_score()
        time.sleep(.2)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    else:
                        self._check_keydown_events(event.key)
            self.play()

    def show_score(self):
        score = self.block.length - 1
        score_str = "Score : {:,}".format(score)
        font = pygame.font.SysFont(None, 48)
        score_image = font.render(score_str, True, self.setting.text_color)
        score_rect = score_image.get_rect()
        score_rect.right = self.window.get_rect().right - 20
        score_rect.top = 20
        self.window.blit(score_image, score_rect)
        pygame.display.flip()


if __name__ == '__main__':
    ai_game = Game()
    ai_game.run()
