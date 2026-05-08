import pygame

class Input:

    # inicializa a classe Input
    def __init__(self, events):
        self.events = events

    # verifica clique de saida do jogo
    def handle_events(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    # verifica clique nas opcoes
    def check_click(self, rects, options):
        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                for i, rect in enumerate(rects):
                    if rect.collidepoint(mouse_position):
                        return options[i]
        return None