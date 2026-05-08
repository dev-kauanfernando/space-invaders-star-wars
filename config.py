import pygame

# configuracoes de tela
class Screen:
    WIDTH = 800
    HEIGHT = 600
    FPS = 60
    TITLE = "A Invasão do Império: O Despertar do Guardião"
    
    def font():
        return pygame.font.Font("./assets/font/PressStart2P-Regular.ttf", 32)

# constantes de cores
class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 203, 50)