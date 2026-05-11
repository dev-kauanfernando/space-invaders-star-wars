import pygame
import config
from src.utils.input import Input

class MainMenu:
    
    # incializa a classe MainMenu
    def __init__(self, screen):
        self.screen = screen
        self.font = config.Screen.FONT
        self.gap = config.Screen.scale(60)
        self.height = config.Screen.scale(-25)
        self.color = config.Colors.YELLOW
        self.options = ["Jogar", "Dificuldade", "Sair"]
        self.rects = []
    
    # lida com entrada
    def handle_input(self, events):
        return Input().check_click(self.rects, self.options, events)
       
    # desenha as opcoes   
    def draw(self):
        total_height = len(self.options) * self.height
        start_y = (config.Screen.HEIGHT - total_height) / 2

        title = self.font.render("Star Wars", False, self.color)
        rect_title = title.get_rect(center=(config.Screen.WIDTH / 2, 150))
        self.screen.blit(title, rect_title)
        
        self.rects = []
        for i, text in enumerate(self.options):
            surface = self.font.render(text, False, self.color)
            rect = surface.get_rect(center=(config.Screen.WIDTH / 2, start_y + i * self.gap))
            self.screen.blit(surface, rect)
            self.rects.append(rect)