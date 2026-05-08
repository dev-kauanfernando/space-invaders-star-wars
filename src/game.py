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
            Input(self.events).handle_events()
            self.draw()
        pygame.quit()
        sys.exit()
    
    # desenha na tela o loop dos eventos do jogo
    def draw(self):
        self.screen.fill(config.Colors.BLACK)
        
        # menu inicial
        if self.state == "menu":
            action = self.scene.main_menu(self.events)
            if action == "Jogar":
                pass
            elif action == "Dificuldade":
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
            if action == "Continuar":
                pass
            elif action == "Voltar ao Menu":
                self.state = "menu"
                self.scene = MainMenu(self.screen)
            elif action == "Sair":
                self.running = False
            
        pygame.display.flip()