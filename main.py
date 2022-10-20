import logging
import sys

import pygame

from screens.fight_screen import FightScreen
from screens.screen import Screen


def initialize_logging() -> None:
    fmt = "%(asctime)s [%(levelname)s] %(message)s"
    logging.basicConfig(format=fmt, level=logging.NOTSET)


def initialize_screen(name: str, size: (int, int) = (720, 480)) -> pygame.Surface:
    pygame.display.set_caption(name)
    return pygame.display.set_mode(size=size)


def quit_game() -> None:
    pygame.quit()
    sys.exit()


initialize_logging()
pygame.init()
surface = initialize_screen("Space game")
current_screens: list[Screen] = [FightScreen()]

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit_game()
    for screen in current_screens:
        screen.handle_events(events)
        screen.render(surface)
    pygame.display.update()
