import pygame.surface

from screens.screen import Screen
from ui.button import Button


class FightScreen(Screen):

    def __init__(self, size: (int, int) = (480, 320)):
        super().__init__(size)
        quit_button = Button((10, 10), (400, 30))
        self.controls.append(quit_button)
