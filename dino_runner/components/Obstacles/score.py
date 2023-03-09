from dino_runner.utils.constants import HAMMER_TYPE
from dino_runner.utils.message_util import print_message


class Score:
    def __init__(self):
        self.score = 0 

    def update(self, game):
        if game.player.type == HAMMER_TYPE:
            self.score += 10
        else:
            self.score += 1
            if self.score % 100 == 0:
                game.game_speed += 2

    def draw(self, screen):
        print_message(f"Score: {self.score}", screen, 950, 30, font_size=24)

    def reset(self):
         self.score = 0