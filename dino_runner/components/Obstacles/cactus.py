import random
from dino_runner.components.Obstacles.Obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle):
    def __init__(self):
        cactus_type = random.randint(0, 2)
        large_cactus_type = random.randint(0, 2)
        large_cactus_image = LARGE_CACTUS[large_cactus_type]
        cactus_image = SMALL_CACTUS[cactus_type]
        cactus = random.choice([cactus_image, large_cactus_image])
        super().__init__(cactus)
        self.rect.bottom = 394


