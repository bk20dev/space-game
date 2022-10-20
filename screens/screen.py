import pygame


class Screen:
    def __init__(self, size: (int, int), navigate):
        self.entities = []
        self.controls = []
        self.navigate = navigate
        self.surface = pygame.surface.Surface(size)

    def render(self, screen: pygame.Surface):
        for entity in self.entities:
            entity.render(self.surface)
        for control in self.controls:
            control.render(self.surface)
        screen.blit(self.surface, (0, 0))

    def handle_events(self, events: list[pygame.event.Event]):
        pass

    def start(self):
        pass

    def stop(self):
        pass
