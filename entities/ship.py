import random
import threading
from entities.laser import Laser
import pygame


class Ship():
    velocity_x = 25
    velocity_y = 5

    def __init__(self, texture, position: [int, int] = (0,0)):
        self.surface = pygame.image.load(texture)
        self.position = [*position]
        self.rect = self.surface.get_rect(topleft=(self.position[0], self.position[1]))
        print(self.surface.get_size())


    def render(self, screen: pygame.Surface):
        screen.blit(self.surface, self.rect)


class PlayerShip(Ship):

    lasers = []

    def movement(self, key):
        if key == pygame.K_LEFT or key == pygame.K_a:
            if self.rect.left - self.velocity_x <= 0:
                self.rect.left = 0
            else:
                self.rect.x = self.rect.x - self.velocity_x
        if key == pygame.K_RIGHT or key == pygame.K_d:
            if self.rect.right + self.velocity_x > 480:
                self.rect.right = 480
            else:
                self.rect.left = self.rect.left + self.velocity_x
        if key == pygame.K_SPACE:
            self.lasers.append(Laser((self.rect.centerx, 240)))


class OpponentShip(Ship):

    health = 100

    def __init__(self, texture):
        super().__init__(texture)
        self.rect.x = random.randint(0, 480 - self.surface.get_size()[0])
        self.movement()

        spawnSounds = [
            "assets/audio/opponentSpawn_001.ogg",
            "assets/audio/opponentSpawn_002.ogg",
        ]

        pygame.mixer.Sound(random.choice(spawnSounds)).play()

    def movement(self):
        threading.Timer(0.1, self.movement).start()
        x = self.rect.x + random.randint(-5, 5)
        if x < 0:
            x = 0
        elif x > 480:
            x = 480 - self.surface.get_size()[0]
        self.rect.x = x
        self.rect.y += self.velocity_y

    def collision(self):
        self.health -= 20

        if self.health == 0:
            deadSounds = [
                "assets/audio/explosionOpponent_001.ogg",
                "assets/audio/explosionOpponent_002.ogg",
                "assets/audio/explosionOpponent_003.ogg",
                "assets/audio/explosionOpponent_004.ogg",
                "assets/audio/explosionOpponent_005.ogg",
            ]
            pygame.mixer.Sound(random.choice(deadSounds)).play()


