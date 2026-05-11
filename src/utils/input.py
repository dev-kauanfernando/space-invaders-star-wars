import pygame

class Input:

    # verifica clique de saida do jogo
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    # verifica clique nas opcoes
    def check_click(self, rects, options, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                for i, rect in enumerate(rects):
                    if rect.collidepoint(mouse_position):
                        return options[i]
        return None