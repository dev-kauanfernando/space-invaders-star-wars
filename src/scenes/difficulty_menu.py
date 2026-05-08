import pygame
import config
from src.utils.input import Input

class DifficultyMenu:
    
    # incializa a classe DifficultyMenu
    def __init__(self, screen):
        self.screen = screen
        self.font = config.Screen.font()
        self.color = config.Colors.YELLOW
        
    # menu de dificuldade
    def difficulty_menu(self, events):
        options = ["Facil", "Medio", "Dificil"]
        total_height = len(options) * -15
        start_y = (config.Screen.HEIGHT - total_height) / 2
        
        rects = []
        for i, text in enumerate(options):
            surface = self.font.render(text, False, self.color)
            rect = surface.get_rect(center=(config.Screen.WIDTH / 2, start_y + i * 75))
            self.screen.blit(surface, rect)
            rects.append(rect)
        return Input(events).check_click(rects, options)