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
            surface = pygame.display.set_mode(
                (info.current_w, info.current_h),
                pygame.FULLSCREEN
            )
        else:
            surface = pygame.display.set_mode(
                (cls._WIDTH, cls._HEIGHT)
            )
            
        cls.WIDTH, cls.HEIGHT = surface.get_size()
        
        scale_x = cls.WIDTH / cls._WIDTH
        scale_y = cls.HEIGHT / cls._HEIGHT
        cls._scale_factor = min(scale_x, scale_y)
        
        if cls.MOBILE:
            cls._scale_factor *= 1.8
        cls.FONT = pygame.font.Font(Path._FONT, cls.scale(26))
        return surface
    
    # ajusta espacamento dos itens presentes na tela    
    @classmethod
    def scale(cls, value):
        return int(value * cls._scale_factor)

# constantes de cores
class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 90, 255)
    YELLOW = (255, 232, 31)
    
# localização dos path
class Path:
    _IMG = os.path.join("assets", "img")
    _FONT = os.path.join("assets", "font", "PressStart2P-Regular.ttf")
    WALLPAPERS = os.path.join(_IMG, "wallpapers")
    SPRITES = os.path.join(_IMG, "sprites")