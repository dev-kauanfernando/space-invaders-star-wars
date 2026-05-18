from src.utils import Render, Assets, Input
from config import Screen, Colors

class Gameplay:
    def __init__(self, screen, difficulty):
        self.screen = screen
        self.difficulty = difficulty
        self.score, self.rect_score = Render.render_text("SCORE", Colors.YELLOW,
            (120, 120)
        )
        self.hit_points, self.rect_hit_points = Assets.hit_points()
        
    def update(self, events):
        return None
        
    def draw(self):
        self.screen.blit(self.score, self.rect_score)
        self.screen.blit(self.hit_points, self.rect_hit_points)