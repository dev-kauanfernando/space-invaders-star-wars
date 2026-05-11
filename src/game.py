import pygame
import sys
import config
from src.scenes.main_menu import MainMenu
from src.scenes.difficulty_menu import DifficultyMenu
from src.scenes.pause_menu import PauseMenu
from src.utils.input import Input

class Game:
    
    # inicializa a classe Game
    def __init__(self):
        pygame.init()
        self.screen = config.Screen.init()
        pygame.display.set_caption(config.Screen.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "menu"
        self.scene = MainMenu(self.screen)
        self.input = Input()
    
    # loop principal    
    def run(self):
        while self.running:
            self.clock.tick(config.Screen.FPS)
            self.events = pygame.event.get()
            self.running = self.input.handle_events(self.events)
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()
    
    # controle de estado
    def update(self):
        action = self.scene.handle_input(self.events)
        
        # menu inicial
        if self.state == "menu":
            if action == "Jogar":
                pass
            elif action == "Dificuldade":
                self.state = "difficulty"
                self.scene = DifficultyMenu(self.screen)
            elif action == "Sair":
                self.running = False
                
        # menu dificuldade
        elif self.state == "difficulty":
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
            if action == "Continuar":
                pass
            elif action == "Voltar ao Menu":
                self.state = "menu"
                self.scene = MainMenu(self.screen)
            elif action == "Sair":
                self.running = False
    
    # desenha cenas na tela
    def draw(self):
        self.screen.fill(config.Colors.BLACK)

        self.scene.draw()
        pygame.display.flip()