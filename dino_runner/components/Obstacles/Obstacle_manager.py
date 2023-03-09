import random
from dino_runner.components.Obstacles.Bird import Bird
from dino_runner.components.Obstacles.cactus import Cactus
from dino_runner.utils.constants import HAMMER_TYPE


class ObstacleManager:
    def __init__(self):
         self.obstacles = []
        
    def update(self, game_speed, player, on_death):
        if not self.obstacles:
            obstacle_types = [Cactus(), Bird()]
            obstacle = random.choice(obstacle_types)
            self.obstacles.append(obstacle)
           
        for obstacle in self.obstacles:
            if player.type == HAMMER_TYPE:
                 obstacle.update(game_speed, self.obstacles, player.rect.x)
            else:
                obstacle.update(game_speed, self.obstacles)
            if obstacle.rect.colliderect(player.rect):
                on_death()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles = []
        self.cactus_points = 0