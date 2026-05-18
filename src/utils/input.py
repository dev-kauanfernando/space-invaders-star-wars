import pygame
from config import Screen

class Input:

    # verifica clique de saida do jogo
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_P:
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
        
    # define a direcao do player no pc
    def keyboard_input(self, player, x, y, speed):
        keys = pygame.key.get_pressed()
        firing = False
        
        if keys[pygame.K_UP] or keys[pygame.K_W]:
            y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_S]:
            y += speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_D]:
            x += speed
        if keys[pygame.K_LEFT] or keys[pygame.K_A]:
            x -= speed
        if keys[pygame.K_SPACE] or pygame.BUTTON_LEFT:
            firing = True
        
        x = max(0, min(x, Screen.WIDTH - player.get_width()))
        y = max(0, min(y, Screen.HEIGHT - player.get_height()))
        
        return x, y, firing