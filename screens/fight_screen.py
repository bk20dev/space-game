import logging
import threading
import random
import pygame

from entities.ship import PlayerShip, OpponentShip
from screens.screen import Screen
from ui.text import Text

opponent_textures = [
    "assets/textures/enemyBlack1.png",
    "assets/textures/enemyBlack2.png",
    "assets/textures/enemyBlack3.png",
    "assets/textures/enemyBlack4.png",
    "assets/textures/enemyBlack5.png",
]


class FightScreen(Screen):
    opponents = []

    def __init__(self, size: (int, int) = (720, 480)):
        super().__init__(size)
        self.ship = PlayerShip("assets/textures/playerShip1_orange.png", (0, 240))
        self.background = pygame.image.load("assets/textures/darkPurple.png")
        self.score_text = Text("", (size[0]-18, 18))
        self.update_score(0)
        self.entities.extend([self.ship])
        self.controls.extend([self.score_text])
        self.generate_opponents()

    def update_score(self, new_score: int):
        self.score_text.text = str(new_score).rjust(6, '0')

    def handle_events(self, events: list[pygame.event.Event]):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                key = event.key
                self.ship.movement(key)

    def render(self, screen: pygame.Surface):
        self.render_background(self.surface)
        super().render(screen)
        for index, laser in enumerate(self.ship.lasers):
            laser.movement()
            self.entities.append(laser)
            for opponent in self.opponents:
                if laser.rect.colliderect(opponent.rect) & laser.alive:
                    logging.debug("collided")
                    laser.collision()
                    opponent.collision()
            if laser.rect.bottom < 0:
                self.ship.lasers.pop(index)

    def render_background(self, surface: pygame.Surface):
        surface_width, surface_height = self.surface.get_size()
        background_width, background_height = self.background.get_size()
        for y in range(0, surface_height, background_height):
            for x in range(0, surface_width, background_width):
                surface.blit(self.background, (x, y))

    def generate_opponents(self):
        threading.Timer(5.0, self.generate_opponents).start()
        opponent_ship = OpponentShip(random.choice(opponent_textures))
        self.entities.append(opponent_ship)
        self.opponents.append(opponent_ship)
