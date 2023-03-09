from pygame import Surface
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image: Surface):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles, player_x_position = 0):
        limit = -self.rect.width
        if player_x_position != 0:
            limit = player_x_position
        self.rect.x -= game_speed
        if self.rect.x < limit:
            obstacles.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
