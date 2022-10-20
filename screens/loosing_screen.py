import pygame

from screens.screen import Screen
from ui.button import Button
from ui.text import Text


class LoosingScreen(Screen):

    def __init__(self, size: (int, int), navigate):
        super().__init__(size, navigate)
        text_player_lost = Text("You lost!", text_size=48, center=(size[0] / 2, size[1] / 2))
        button_back = Button((196, 32), (0, 0), text="Play again", centerx=size[0] / 2, top=(size[1] / 2 + 36))
        self.controls.extend([text_player_lost, button_back])
        pygame.mixer.Sound("assets/audio/game_over.wav").play()

    def render(self, screen: pygame.Surface):
        self.surface.fill("#3a2e3f")
        super().render(screen)
        screen.blit(self.surface, self.surface.get_size())
