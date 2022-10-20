import random
import pygame
from threading import Timer


class Laser:
    power = 20
    velocity = 1
    alive = True

    def __init__(self, position: (int, int) = (0, 0)):
        self.surface = pygame.image.load("assets/textures/laserBlue05.png")
        self.position = [*position]
        self.rect = self.surface.get_rect(topleft=(self.position[0], self.position[1]))
        shotSounds = [
            "assets/audio/laserSmall_000.ogg",
            "assets/audio/laserSmall_001.ogg",
            "assets/audio/laserSmall_002.ogg",
            "assets/audio/laserSmall_003.ogg",
            "assets/audio/laserSmall_004.ogg",
        ]
        pygame.mixer.Sound(random.choice(shotSounds)).play()

    def render(self, screen: pygame.Surface):
        screen.blit(self.surface, self.rect)

    def movement(self):
        self.rect.y -= self.velocity

    def anihilate(self):
        self.rect.bottom = -10

    def collision(self):
        explosionEffects = [
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

        explosionEffect = random.choice(explosionEffects)

        self.surface = pygame.image.load(explosionEffect["first"])
        self.surface = pygame.image.load(explosionEffect["second"])
        t = Timer(0.05, self.anihilate)
        t.start()
        self.alive=False


