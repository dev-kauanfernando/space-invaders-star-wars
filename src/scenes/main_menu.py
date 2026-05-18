from config import Colors
from src.utils import Input, Assets, Render

class MainMenu:
    
    # incializa a classe MainMenu
    def __init__(self, screen):
        self.screen = screen
        self.input = Input()
        self.options = ["JOGAR", "DIFICULDADE", "SAIR"]
        self.surfaces, self.rects = Render.render_options(self.options, Colors.YELLOW, 200)
        self.title, self.rect_title = Assets.title()
        self.player, self.rect_player = Assets.player()
    
    # lida com entrada
    def update(self, events):
        return self.input.check_click(self.rects, self.options, events)
       
    # desenha as opcoes   
    def draw(self):
        self.screen.blit(self.title, self.rect_title)
        self.screen.blit(self.player, self.rect_player)
        
        for surface, rect in zip(self.surfaces, self.rects):
            self.screen.blit(surface, rect)