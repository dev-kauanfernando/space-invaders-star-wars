import pygame
import config
from src.utils.input import Input

class MainMenu:
    
    # incializa configuracoes do main_menu(self)
    def __init__(self, screen):
        self.screen = screen
        self.font = config.Screen.font()
        self.color = config.Colors.YELLOW
        
    # menu principal    
    def main_menu(self, events):
        options = ["Jogar", "Dificuldade", "Sair"]
        total_height = len(options) * 50
        start_y = (config.Screen.HEIGHT - total_height) / 2
        
        rects = []
        for i, text in enumerate(options):
            surface = self.font.render(text, False, self.color)
            rect = surface.get_rect(center=(config.Screen.WIDTH / 2, start_y + i * 100))
            self.screen.blit(surface, rect)
            rects.append(rect)
        return Input.check_click(rects, options, events)