import pygame

text_color = (255, 255, 255, 255)


class Text:
    def __init__(self, text: str = "", position: (int, int) = (0, 0), text_size: int = 24, **kwargs):
        self.position = position
        self.text = text
        self.font = pygame.font.SysFont("assets/fonts/kenvector_future.ttf", text_size)
        self.kwargs = kwargs

    def render(self, screen: pygame.Surface):
        score_surface = self.font.render(self.text, True, text_color)
        score_rect = score_surface.get_rect(**self.kwargs)
        screen.blit(score_surface, score_rect)
