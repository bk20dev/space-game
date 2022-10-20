import pygame


class Screen:
    entities = []
    controls = []

    def __init__(self, size: (int, int)):
        self.surface = pygame.surface.Surface(size)

    def render(self, screen: pygame.Surface):
        for entity in self.entities:
            entity.render(self.surface)
        for control in self.controls:
            control.render(self.surface)
        screen.blit(self.surface, (0, 0))

    def handle_events(self, events: list[pygame.event.Event]):
        pass
