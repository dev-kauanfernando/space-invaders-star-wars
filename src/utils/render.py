import pygame
import os
from config import Screen, Colors, Path

class Assets:
    @staticmethod
    def safe_load(path, size, fallback_color):
        try:
            img = pygame.image.load(path).convert_alpha()
        except (pygame.error, FileNotFoundError):
            img = pygame.Surface(size)
            img.fill(fallback_color)
        return pygame.transform.scale(img, size)
        
    @staticmethod
    def background():
        img = Assets.safe_load(
            os.path.join(Path.WALLPAPERS, "background.png"),
            (Screen.scale(800), Screen.scale(600)),
            Colors.BLACK
        )
        background = pygame.Surface(
            (Screen.WIDTH, Screen.HEIGHT)
        )
        for x in range(0, Screen.WIDTH, img.get_width()):
            for y in range(0, Screen.HEIGHT, img.get_height()):
                background.blit(img, (x, y))
        return background
    
    @staticmethod
    def title():
        img = Assets.safe_load(
            os.path.join(Path.WALLPAPERS, "star-wars-logo.png"),
            (Screen.scale(380), Screen.scale(160)),
            Colors.YELLOW
        )
        rect_img = img.get_rect(
            center=(Screen.WIDTH / 2, Screen.scale(125))
        )
        return img, rect_img
    
    @staticmethod
    def player():
        img= Assets.safe_load(
            os.path.join(Path.SPRITES, "player.png"),
            (Screen.scale(64), Screen.scale(64)),
            Colors.WHITE
        )
        rect_img = img.get_rect(
            centerx=Screen.WIDTH / 2, bottom=Screen.scale(580)
        )
        return img, rect_img
    
    @staticmethod
    def enemy():
        img = Assets.safe_load(
            os.path.join(Path.SPRITES, "enemy.png"),
            (Screen.scale(32), Screen.scale(32)),
            Colors.RED
        )
        rect_img = img.get_rect(
            center=(Screen.WIDTH / 2, Screen.scale(125))
        )
        return img, rect_img
    
    @staticmethod
    def boss():
        img = Assets.safe_load(
            os.path.join(Path.SPRITES, "boss.png"),
            (Screen.scale(96), Screen.scale(96)),
            Colors.RED
        )
        rect_img = img.get_rect(
            center=(Screen.WIDTH / 2, Screen.scale(125))
        )
        return img, rect_img
    
    @staticmethod
    def laser():
        img = Assets.safe_load(
            os.path.join(Path.SPRITES, "laser.png"),
            (Screen.scale(6), Screen.scale(20)),
            Colors.BLUE
        )
        rect_img = img.get_rect(
            center=(Screen.WIDTH / 2, Screen.scale(125))
        )
        return img, rect_img
    
    @staticmethod
    def bacta():
        img = Assets.safe_load(
            os.path.join(Path.SPRITES, "bacta.png"),
            (Screen.scale(32), Screen.scale(32)),
            Colors.BLUE
        )
        rect_img = img.get_rect(
            center=(Screen.WIDTH / 2, Screen.scale(125))
        )
        return img, rect_img
    
    @staticmethod
    def hit_points():
        img = Assets.safe_load(
            os.path.join(Path.SPRITES, "hit_points.png"),
            (Screen.scale(16), Screen.scale(16)),
            Colors.RED
        )
        rect_img = img.get_rect(
            x=(Screen.scale(120)), bottom=(Screen.scale(580))
        )
        return img, rect_img
    
class Render:
    @staticmethod
    def render_text(text, color, position):
        surface = Screen.FONT.render(text, False, color)
        rect = surface.get_rect(center=position)
        return surface, rect
    
    @staticmethod
    def render_options(options, color, offset):
        surfaces, rects = [], []
        for i, text in enumerate(options):
            surface, rect = Render.render_text(text, color, (
                Screen.WIDTH / 2,
                (Screen.HEIGHT / 2 + offset) 
                + i * Screen.scale(60)
                ))
            surfaces.append(surface)
            rects.append(rect)
        return surfaces, rects