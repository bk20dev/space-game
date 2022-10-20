import random
from threading import Timer

import pygame


class Laser:
    power = 20
    velocity = 2
    alive = True

    def __init__(self, position: (int, int) = (0, 0)):
        self.surface = pygame.image.load("assets/textures/laserBlue05.png")
        self.position = [*position]
        self.rect = self.surface.get_rect(topleft=(self.position[0], self.position[1]))
        shot_sounds = [
            "assets/audio/laserSmall_000.ogg",
            "assets/audio/laserSmall_001.ogg",
            "assets/audio/laserSmall_002.ogg",
            "assets/audio/laserSmall_003.ogg",
            "assets/audio/laserSmall_004.ogg",
        ]
        pygame.mixer.Sound(random.choice(shot_sounds)).play()

    def render(self, screen: pygame.Surface):
        screen.blit(self.surface, self.rect)

    def movement(self):
        self.rect.y -= self.velocity

    def destroy(self):
        self.rect.bottom = -10

    def collision(self):
        explosion_effects = [
            {
                "first": "assets/textures/laserExplosion04.png",
                "second": "assets/textures/laserExplosion01.png",
            },
            {
                "first": "assets/textures/laserExplosion02.png",
                "second": "assets/textures/laserExplosion03.png",
            }
        ]

        pygame.mixer.Sound("assets/audio/laser_explosion_001.ogg").play()

        explosion_effect = random.choice(explosion_effects)

        self.surface = pygame.image.load(explosion_effect["first"])
        self.surface = pygame.image.load(explosion_effect["second"])
        t = Timer(0.05, self.destroy)
        t.start()
        self.alive = False
