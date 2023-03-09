import random
from pygame import Surface
from pygame.sprite import Sprite

from dino_runner.utils.constants import HEART_TYPE, SCREEN_WIDTH


class PowerUp(Sprite):
    def __init__(self, image: Surface, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)
        self.type = type
        if type == HEART_TYPE:
            self.duration = 3
        else:
            self.duration = random.randint(5, 8) #tiempo de cuanto va aestar activo
        self.start_time = 0 #En que momento a sido agarrado el power up

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))