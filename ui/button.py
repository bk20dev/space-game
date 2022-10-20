import pygame


class Button:
    def __init__(self, size: (int, int), position: (int, int) = (0, 0), text: str = "", text_size: int = 24, **kwargs):
        self.surface = pygame.surface.Surface(size)
        self.font = pygame.font.SysFont("assets/fonts/kenvector_future.ttf", text_size)
        self.position = position
        self.kwargs = kwargs
        self.text = text

    def render(self, screen: pygame.Surface):
        self.surface.fill("white")
        button_rect = self.surface.get_rect(**self.kwargs)
        text_surface = self.font.render(self.text, True, (0, 0, 0, 255))
        width, height = self.surface.get_size()
        text_rect = text_surface.get_rect(center=(width / 2, height / 2))
        self.surface.blit(text_surface, text_rect)
        screen.blit(self.surface, button_rect)

    def is_clicked(self, mouse: (int, int)) -> bool:
        px, py = self.position
        width, height = self.surface.get_size()
        return mouse[0] in range(px, px + width) and mouse[1] in range(py, py + height)
