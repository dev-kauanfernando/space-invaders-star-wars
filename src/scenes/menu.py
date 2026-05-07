import pygame
import config

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("arial", 50)
        self.color = config.Colors.RED
        
    # Menu principal    
    def main_menu(self):
        options = ["Jogar", "Sair"]
        total_height = len(options) * 50
        start_y = (config.Screen.HEIGHT - total_height) / 2
        
        for i, text in enumerate(options):
            surface = self.font.render(text, False, self.color)
            rect = surface.get_rect(center=(config.Screen.WIDTH / 2, start_y + i * 100))
            self.screen.blit(surface, rect)