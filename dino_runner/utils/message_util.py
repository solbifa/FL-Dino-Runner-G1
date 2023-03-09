import pygame
import os

from dino_runner.utils.constants import FONT_STYLE


#class Message: 
def print_message(message, screen, x_position, y_position, font_style = FONT_STYLE, font_size = 32, font_color = (0, 0, 0)):
    font = pygame.font.Font(font_style, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (x_position, y_position)
    screen.blit(text, text_rect)
