import logging
import threading
import random
import pygame
from threading import Timer

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
    points = 0
    health = 0

    def __init__(self, window_size: (int, int), navigate):
        super().__init__(window_size, navigate)
        self.window_size = window_size
        self.ship = PlayerShip("assets/textures/playerShip1_orange.png", window_size, (0, 0))
        self.background = pygame.image.load("assets/textures/darkPurple.png")
        self.score_text = Text("", topright=(window_size[0] - 18, 18))
        self.health_text = Text("", topleft=(18, 18))
        self.update_score(0)
        self.update_health(100)
        self.entities.extend([self.ship])
        self.controls.extend([self.score_text])
        self.controls.extend([self.health_text])
        self.generate_opponents()

    def update_score(self, new_score: int):
        self.score_text.text = str(new_score).rjust(6, '0')

    def add_points(self, amount: int):
        self.points += amount
        self.update_score(self.points)

    def update_health(self, new_health: int):
        self.health_text.text = str(new_health)

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
                if laser.rect.colliderect(opponent.rect) and laser.alive:
                    self.add_points(10)
                    logging.debug("collided")
                    laser.collision()
                    dead = opponent.collision()
                    if dead:
                        self.add_points(50)
            if laser.rect.bottom < 0:
                self.ship.lasers.pop(index)

        for opponent in self.opponents:
            if opponent.rect.bottom > self.window_size[1] and not opponent.caused_damage:
                opponent.caused_damage = True
                self.health -= 20
                if self.health >= 0:
                    self.update_health(self.health)
                else:
                    self.navigate("death")

    def render_background(self, surface: pygame.Surface):
        surface_width, surface_height = self.surface.get_size()
        background_width, background_height = self.background.get_size()
        for y in range(0, surface_height, background_height):
            for x in range(0, surface_width, background_width):
                surface.blit(self.background, (x, y))

    def generate_opponents(self):
        threading.Timer(5.0, self.generate_opponents).start()
        opponent_ship = OpponentShip(random.choice(opponent_textures), self.window_size)
        self.entities.append(opponent_ship)
        self.opponents.append(opponent_ship)
