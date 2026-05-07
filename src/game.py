import pygame
import sys
import config
from src.scenes.menu import Menu

class Game:
    # Inicializar configurações
    def __init__(self):
        self.screen = pygame.display.set_mode((config.Screen.WIDTH, config.Screen.HEIGHT))
        pygame.display.set_caption(config.Screen.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.menu = Menu(self.screen)
    
    # Loop principal    
    def run(self):
        while self.running:
            self.clock.tick(config.Screen.FPS)
            self.handle_events()
            self.draw()
        pygame.quit()
        sys.exit()
    
    # Eventos na tela    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    # Desenhar na tela
    def draw(self):
        self.screen.fill(config.Colors.WHITE)
        self.menu.main_menu()
        pygame.display.flip()