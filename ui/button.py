import logging

import pygame


class Button:
    def __init__(self, size: (int, int), position: (int, int) = (0, 0)):
        self.surface = pygame.surface.Surface(size)
        self.position = position

    def render(self, screen: pygame.Surface):
        self.surface.fill("white")
        screen.blit(self.surface, self.position)

    def is_clicked(self, mouse: (int, int)) -> bool:
        px, py = self.position
        width, height = self.surface.get_size()
        return mouse[0] in range(px, px+width) and mouse[1] in range(py, py+height)
