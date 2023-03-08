import random
from dino_runner.components.Obstacles.Obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle):
    def __init__(self):
        cactus_type = random.randint(0, 2)
        image = SMALL_CACTUS[cactus_type]
        super().__init__(image)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self):
        large_cactus_type = random.randint(0, 2)
        image = LARGE_CACTUS[large_cactus_type]
        super().__init__(image)
        self.rect.y = 300
