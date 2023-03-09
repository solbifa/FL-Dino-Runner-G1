import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_HAMMER, DUCKING_SHIELD, HAMMER_TYPE, HEART_TYPE, \
    JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING, RUNNING_HAMMER, RUNNING_SHIELD, SCREEN_WIDTH, SHIELD_TYPE
from dino_runner.utils.message_util import print_message

DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"

DUCK_IMG ={ DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, HEART_TYPE: DUCKING}
JUMP_IMG ={ DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, HEART_TYPE: JUMPING}
RUN_IMG ={ DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, HEART_TYPE: RUNNING}

class Dinosaur(Sprite):
    POSITION_X = 80
    POSITION_y = 310
    JUMP_VELOCITY = 8.5
    COORDENADA_DUCK = 340

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.image = RUN_IMG[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_y

        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0
        self.lives = 3

    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()

        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING

        if self.step >= 10:
            self.step = 0

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        print("VELOCITY ::", self.jump_velocity)
        print("y ::", self.rect.y)
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = DINO_RUNNING
            self.rect.y = self.POSITION_y 

    def duck(self):
        print("Ducking")
        self.image = DUCK_IMG[self.type][self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.COORDENADA_DUCK
        self.step += 1

    def run(self):
        self.image = RUN_IMG[self.type][self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_y
        self.step += 1

    def draw(self, screen):
        print_message(f"Lives: {self.lives}", screen, 950, 55, font_size=24)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, power_up):
        self.type = power_up.type
        self.power_up_time_up = power_up.start_time + \
            (power_up.duration * 1000)
        if self.type == HEART_TYPE:
            self.lives += 1

    def check_power_up(self, screen):
        time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
        if time_to_show >= 0:
            half_screen_width = SCREEN_WIDTH // 2
            if self.type == SHIELD_TYPE:
                print_message(f"{self.type.capitalize()}enabled for {time_to_show} seconds.", screen, half_screen_width, 50, font_size=16)
            elif self.type == HAMMER_TYPE:
                print_message(f"{self.type.capitalize()} enabled for {time_to_show} seconds. Hit cacti to earn extra points!", 
                        screen, half_screen_width, 50, font_size=16)
            elif self.type == HEART_TYPE:
                print_message("You win an extra live.", screen, half_screen_width, 50, font_size=16)
            else:
                print_message("Unknown power-up!", screen, half_screen_width, 50, font_size=16)
        else:
            self.type = DEFAULT_TYPE
            self.power_up_time_up = 0
