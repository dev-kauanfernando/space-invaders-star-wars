from config import Colors
from src.utils import Input, Render

class DifficultyMenu:
    
    # incializa a classe DifficultyMenu
    def __init__(self, screen):
        self.screen = screen
        self.options = ["FACIL", "MEDIO", "DIFICIL"]
        self.surfaces, self.rects = Render.render_options(self.options, Colors.YELLOW, 0)
        
    # lida com entrada
    def update(self, events):
        return Input().check_click(self.rects, self.options, events)
       
    # desenha as opcoes   
    def draw(self):
        for surface, rect in zip(self.surfaces, self.rects):
            self.screen.blit(surface, rect)