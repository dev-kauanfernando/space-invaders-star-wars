import pygame
import sys
import config
from src.scenes.main_menu import MainMenu
from src.scenes.difficulty_menu import DifficultyMenu
from src.scenes.pause_menu import PauseMenu

class Game:
    
    # inicializa configuracoes
    def __init__(self):
        self.screen = pygame.display.set_mode((config.Screen.WIDTH, config.Screen.HEIGHT))
        pygame.display.set_caption(config.Screen.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "menu"
        self.scene = MainMenu(self.screen)
    
    # loop principal    
    def run(self):
        while self.running:
            self.clock.tick(config.Screen.FPS)
            self.events = pygame.event.get()
            self.handle_events(self.events)
            self.draw(self.events)
        pygame.quit()
        sys.exit()
    
    # captura eventos na tela    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    # desenha na tela
    def draw(self, events):
        self.screen.fill(config.Colors.BLACK)
        
        # menu inicial
        if self.state == "menu":
            action = self.scene.main_menu(self.events)
            if action == "Dificuldade":
                self.state = "difficulty"
                self.scene = DifficultyMenu(self.screen)
            elif action == "Sair":
                self.running = False
        # menu dificuldade
        elif self.state == "difficulty":
            action = self.scene.difficulty_menu(self.events)
            if action == "Facil":
                self.state = "menu"
                self.scene = MainMenu(self.screen)
            elif action == "Medio":
                self.state = "menu"
                self.scene = MainMenu(self.screen)
            elif action == "Dificil":
                self.state = "menu"
                self.scene = MainMenu(self.screen)
        # menu de pausa
        elif self.state == "pause":
            action = self.scene.pause_menu(self.events)
        pygame.display.flip()