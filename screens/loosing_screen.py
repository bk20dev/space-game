import pygame

from screens.screen import Screen
from ui.button import Button
from ui.text import Text


class LoosingScreen(Screen):

    def __init__(self, size: (int, int), navigate):
        super().__init__(size, navigate)
        text_player_lost = Text("You lost!", text_size=48, center=(size[0] / 2, size[1] / 2))
        self.button_back = Button((196, 32), text="Play again", centerx=size[0] / 2, top=(size[1] / 2 + 36))
        self.controls.extend([text_player_lost, self.button_back])
        pygame.mixer.Sound("assets/audio/game_over.wav").play()

    def render(self, screen: pygame.Surface):
        self.surface.fill("#3a2e3f")
        super().render(screen)
        screen.blit(self.surface, self.surface.get_size())

    def handle_events(self, events: list[pygame.event.Event]):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN \
                    and self.button_back.is_clicked(pygame.mouse.get_pos()):
                self.navigate("game")
