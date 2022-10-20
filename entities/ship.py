import random
import threading

import pygame

from entities.laser import Laser


class Ship:
    velocity_x = 25
    velocity_y = 20

    def __init__(self, texture, window_size: (int, int), position: [int, int] = (0, 0)):
        self.surface = pygame.image.load(texture)
        self.position = [*position]
        self.window_size = window_size
        self.rect = self.surface.get_rect(topleft=(self.position[0], self.position[1]))
        print(self.surface.get_size())

    def render(self, screen: pygame.Surface):
        screen.blit(self.surface, self.rect)


class PlayerShip(Ship):
    lasers = []

    def __init__(self, texture, window_size: (int, int), position: [int, int] = (0, 0)):
        super().__init__(texture, window_size, position)
        self.rect = self.surface.get_rect(bottomleft=(position[0], self.window_size[1]))

    def movement(self, key):
        window_width = self.window_size[0]

        if key == pygame.K_LEFT or key == pygame.K_a:
            if self.rect.left - self.velocity_x <= 0:
                self.rect.left = 0
            else:
                self.rect.x = self.rect.x - self.velocity_x
        if key == pygame.K_RIGHT or key == pygame.K_d:
            if self.rect.right + self.velocity_x > window_width:
                self.rect.right = window_width
            else:
                self.rect.left = self.rect.left + self.velocity_x
        if key == pygame.K_SPACE:
            self.lasers.append(Laser((self.rect.centerx, self.rect.top)))

    def damage(self):
        pygame.mixer.Sound("assets/audio/impactPunch_heavy_001.ogg").play()


class OpponentShip(Ship):
    health = 100
    caused_damage = False

    def __init__(self, texture, window_size: (int, int), position: [int, int] = (0, 0)):
        super().__init__(texture, window_size, position)
        self.rect.x = random.randint(0, self.window_size[0] - self.surface.get_size()[0])
        self.movement_x()
        self.movement_y()

        spawn_sounds = [
            "assets/audio/opponentSpawn_001.ogg",
            "assets/audio/opponentSpawn_002.ogg",
        ]

        pygame.mixer.Sound(random.choice(spawn_sounds)).play()

    def movement_x(self):
        window_width, window_height = self.window_size
        threading.Timer(0.2, self.movement_x).start()
        x = self.rect.x + random.randint(-15, 15)
        if x < 0:
            x = 0
        elif x > window_width:
            x = window_width - self.surface.get_size()[0]
        self.rect.x = x

    def movement_y(self):
        threading.Timer(0.5, self.movement_y).start()
        self.rect.y += self.velocity_y

    def anihilate(self):
        self.caused_damage = True
        self.rect.top = self.window_size[1] + 10

    def collision(self) -> bool:
        self.health -= 20

        if self.health == 0:
            death_sounds = [
                "assets/audio/explosionOpponent_001.ogg",
                "assets/audio/explosionOpponent_002.ogg",
                "assets/audio/explosionOpponent_003.ogg",
                "assets/audio/explosionOpponent_004.ogg",
                "assets/audio/explosionOpponent_005.ogg",
            ]
            pygame.mixer.Sound(random.choice(death_sounds)).play()
            self.surface = pygame.image.load("assets/textures/ship_explosion1.png")
            t = threading.Timer(0.2, self.anihilate)
            t.start()
            return True
        return False
