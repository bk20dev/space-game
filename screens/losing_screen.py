import pygame

from screens.screen import Screen
from ui.text import Text


class LosingScreen(Screen):

    def __init__(self, size: (int, int), navigate):
        super().__init__(size, navigate)
        self.text = Text("You lose!", (size[0] - 18, 18))
        pygame.mixer.Sound("assets/audio/game_over.wav").play()

    def render(self, screen: pygame.Surface):
        super().render(screen)
