import logging
import random
import threading

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
    points = 0
    health = 0

    def __init__(self, window_size: (int, int), navigate):
        super().__init__(window_size, navigate)
        self.window_size = window_size
        self.player = PlayerShip("assets/textures/playerShip1_orange.png", window_size, (0, 0))
        self.background_image = pygame.image.load("assets/textures/darkPurple.png")
        self.health_text = Text("", topleft=(18, 18))
        self.score_text = Text("", topright=(window_size[0] - 18, 18))
        self.entities.extend([self.player])
        self.controls.extend([self.score_text, self.health_text])
        self.opponent_timer = None

    def update_score(self, new_score: int):
        self.score_text.text = str(new_score).rjust(6, '0')

    def add_points(self, amount: int):
        self.points += amount
        self.update_score(self.points)

    def update_health(self, new_health: int):
        self.health_text.text = str(new_health) + "%"

    def add_health(self, amount: int):
        self.health += amount
        self.update_health(self.health)

    def handle_events(self, events: list[pygame.event.Event]):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                key = event.key
                self.player.movement(key)

    def render(self, screen: pygame.Surface):
        self.render_background(self.surface)
        super().render(screen)
        for index, laser in enumerate(self.player.lasers):
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
                self.player.lasers.pop(index)

        for opponent in self.opponents:
            if opponent.rect.bottom > self.window_size[1] and not opponent.caused_damage:
                opponent.caused_damage = True
                self.add_health(-20)
                if self.health <= 0:
                    self.navigate("death")

    def start(self):
        self.update_score(0)
        self.update_health(100)
        self.generate_opponents()

    def stop(self):
        if self.opponent_timer is not None:
            self.opponent_timer.cancel()

    def render_background(self, surface: pygame.Surface):
        surface_width, surface_height = self.surface.get_size()
        background_width, background_height = self.background_image.get_size()
        for y in range(0, surface_height, background_height):
            for x in range(0, surface_width, background_width):
                surface.blit(self.background_image, (x, y))

    def generate_opponents(self):
        self.opponent_timer = threading.Timer(5.0, self.generate_opponents)
        self.opponent_timer.start()
        opponent_ship = OpponentShip(random.choice(opponent_textures), self.window_size)
        self.entities.append(opponent_ship)
        self.opponents.append(opponent_ship)
