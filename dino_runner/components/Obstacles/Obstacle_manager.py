import random
import pygame
from dino_runner.components.Obstacles.Bird import Bird
from dino_runner.components.Obstacles.cactus import Cactus
from dino_runner.components.Obstacles.cactus import LargeCactus


class ObstacleManager:
    def __init__(self):
         self.obstacles = []
        
    def update(self, game_speed, player, on_death):
        if not self.obstacles:
            obstacle_types = [Cactus(), LargeCactus(), Bird()]
            obstacle = random.choice(obstacle_types)
            self.obstacles.append(obstacle)
           
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                on_death()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles = []