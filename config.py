import pygame
import os

# configuracoes de tela
class Screen:
    FPS = 60
    TITLE = "A Invasão do Império: O Despertar do Guardião"
    MOBILE_BREAKPOINT = 600
    _WIDTH = 800
    _HEIGHT = 600
    
    # ajusta o layout de acordo a dimensao da tela
    @classmethod
    def init(cls):
        cls.MOBILE = os.path.exists("/data/data/ru.iiec.pydroid3")
        
        if cls.MOBILE:
            info = pygame.display.Info()
            surface = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
        else:
            surface = pygame.display.set_mode((cls._WIDTH, cls._HEIGHT))
    
        cls.WIDTH, cls.HEIGHT = surface.get_size()
        cls._update_font()
        cls.layout()
        return surface
    
    # ajusta espacamento dos itens presentes na tela    
    @classmethod
    def layout(cls):
        if cls.MOBILE:
            cls.GAP = 100
        else:
            cls.GAP = 75
    
    # ajusta o tamanho da fonte de acordo a dimensao da tela
    @classmethod
    def _update_font(cls):
        path = os.path.join("assets", "font", "PressStart2P-Regular.ttf")
        if cls.MOBILE:
            cls.FONT = pygame.font.Font(path, 48)
        else:
            cls.FONT = pygame.font.Font(path, 32)

# constantes de cores
class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 203, 50)