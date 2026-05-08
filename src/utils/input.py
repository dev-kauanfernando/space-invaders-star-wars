import pygame

class Input:
    
    # verifica clique nas opcoes
    def check_click(rects, options, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                for i, rect in enumerate(rects):
                    if rect.collidepoint(mouse_position):
                        return options[i]
        return None