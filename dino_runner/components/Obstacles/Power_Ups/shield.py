from dino_runner.components.Obstacles.Power_Ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE, HEART, HEART_TYPE, SHIELD, SHIELD_TYPE


class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)

class Heart(PowerUp):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)

class Hammer(PowerUp):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
