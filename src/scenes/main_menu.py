import pygame
import os
import config
from src.utils.input import Input

class MainMenu:
    
    # incializa a classe MainMenu
    def __init__(self, screen):
        self.screen = screen
        self.font = config.Screen.FONT
        self.item_height = config.Screen.ITEM_HEIGHT
        self.color = config.Colors.YELLOW
        self.options = ["Jogar", "Dificuldade", "Sair"]
        self.rects = []
        self.title = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "img", "star-wars-logo.png")).convert_alpha(),
            (config.Screen.scale(512), config.Screen.scale(220))
        )
        self.rect_title = self.title.get_rect(center=(config.Screen.WIDTH / 2,  config.Screen.scale(300)))
    
    # lida com entrada
    def handle_input(self, events):
        return Input().check_click(self.rects, self.options, events)
       
    # desenha as opcoes   
    def draw(self):
        self.screen.blit(self.title, self.rect_title)
        total_height = len(self.options) * self.item_height
        start_y = (config.Screen.HEIGHT - total_height) / 2 + config.Screen.scale(100)
        
        self.rects = []
        for i, text in enumerate(self.options):
            surface = self.font.render(text, False, self.color)
            rect = surface.get_rect(center=(config.Screen.WIDTH / 2, start_y + i * self.item_height))
            self.screen.blit(surface, rect)
            self.rects.append(rect)