import random
from dino_runner.components.Obstacles.Obstacle import Obstacle

from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    BIRD_DOWN = 320
    BIRD_MIDDLE = 260
    BIRD_UPPER = 220

    def __init__(self):
        image = BIRD[0]
        super().__init__(image)
        self.rect.y = random.choice([self.BIRD_UPPER, self.BIRD_MIDDLE, self.BIRD_DOWN])  # elegir posición aleatoria en y
        self.flutter = 0
    
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        self.image = BIRD[self.flutter // 5]
        self.flutter += 1
        if self.flutter >= 10:
            self.flutter = 0

        if self.rect.x < -self.rect.width:
            obstacles.remove(self)

        