import pygame
from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.components.Obstacles.Obstacle_manager import ObstacleManager
from dino_runner.components.Obstacles.Power_Ups.power_up_manager import PowerUpManager
from dino_runner.components.Obstacles.score import Score

from dino_runner.utils.constants import BG, DINO_START, FONT_STYLE_CONSOLE, GAME_OVER, HAMMER_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS
from dino_runner.utils.message_util import print_message


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.max_score = 0
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.death_count = 0
        self.power_up_manager = PowerUpManager()

    def run(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def start_game(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset()
        self.power_up_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.score.score, self.player)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player.check_power_up(self.screen)
        #pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def on_death(self):
        is_invincible = self.player.type == SHIELD_TYPE or self.player.type == HAMMER_TYPE
        if not is_invincible:
            pygame.time.delay(500)
            self.playing = False
            self.death_count  += 1
            self.player.lives -= 1
            if self.score.score > self.max_score:
                self.max_score = self.score.score

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if not self.death_count:
            print_message("Welcome, press any key to start!", self.screen, half_screen_width, half_screen_height, FONT_STYLE_CONSOLE)
        elif self.player.lives == 0:
            self.screen.blit(GAME_OVER, (half_screen_width - 200, half_screen_height))
        else:
            print_message("Restarting game...", self.screen, half_screen_width, half_screen_height, font_color=(0, 255, 0))
            print_message(f"Deaths: {self.death_count}", self.screen, half_screen_width, half_screen_height + 50)
            print_message(f"Score: {self.score.score}", self.screen, half_screen_width, half_screen_height + 100)
            print_message(f"Lives: {self.player.lives}", self.screen, half_screen_width, half_screen_height + 150)
            print_message(f"Max score: {self.max_score}", self.screen, half_screen_width, half_screen_height + 200)
            
        self.screen.blit(DINO_START, (half_screen_width - 40, half_screen_height - 140))
        pygame.display.update()
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

            elif event.type == pygame.KEYDOWN:
                self.score.reset()
                if self.player.lives == 0:
                    self.player.lives = 3
                self.start_game()

