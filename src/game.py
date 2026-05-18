import pygame
import sys
import os
from config import Screen, Colors
from src.scenes import MainMenu, DifficultyMenu, PauseMenu, Gameplay
from src.utils import Input, Assets

class Game:
    
    # inicializa a classe Game
    def __init__(self):
        pygame.init()
        self.screen = Screen.init()
        pygame.display.set_caption(Screen.TITLE)
        self.background = Assets.background()
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "menu"
        self.scenes = {
            "gameplay": Gameplay(self.screen, difficulty=1),
            "menu": MainMenu(self.screen),
            "difficulty": DifficultyMenu(self.screen),
            "pause": PauseMenu(self.screen)
        }
        self.scene = self.scenes["menu"]
        self.input = Input()
    
    # loop principal    
    def run(self):
        while self.running:
            self.clock.tick(Screen.FPS)
            self.events = pygame.event.get()
            self.running = self.input.handle_events(self.events)
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()
    
    # controle de estado
    def update(self):
        action = self.scene.update(self.events)
        
        # menu inicial
        if self.state == "menu":
            if action == "JOGAR":
                self.state = "gameplay"
                self.scene = self.scenes["gameplay"]
            elif action == "DIFICULDADE":
                self.state = "difficulty"
                self.scene = self.scenes["difficulty"]
            elif action == "SAIR":
                self.running = False
    
        # menu dificuldade
        elif self.state == "difficulty":
            if action == "FACIL":
                self.state = "menu"
                self.scene = self.scenes["menu"]
            elif action == "MEDIO":
                self.state = "menu"
                self.scene = self.scenes["menu"]
            elif action == "DIFICIL":
                self.state = "menu"
                self.scene = self.scenes["menu"]
                
        # menu de pausa
        elif self.state == "pause":
            if action == "CONTINUAR":
                pass
            elif action == "VOLTAR AO MENU":
                self.state = "menu"
                self.scene = self.scenes["menu"]
            elif action == "SAIR":
                self.running = False
                
        elif self.state == "gameplay":
            if action:
                self.state = "pause"
                self.scene = self.scenes["pause"]
    
    # desenha cenas na tela
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.scene.draw()
        pygame.display.flip()