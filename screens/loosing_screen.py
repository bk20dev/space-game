import pygame

from screens.screen import Screen
from ui.text import Text


class LoosingScreen(Screen):

    def __init__(self, size: (int, int), navigate):
        super().__init__(size, navigate)
        text = Text("You lose!", topleft=(size[0] / 2, 18))
        self.controls.append(text)
        pygame.mixer.Sound("assets/audio/game_over.wav").play()

    def render(self, screen: pygame.Surface):
        self.surface.fill("red")
        super().render(screen)
        screen.blit(self.surface, self.surface.get_size())
