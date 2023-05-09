import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.pos = pygame.math.Vector2((lib.SCREEN_WIDTH / 2), (lib.SCREEN_HEIGHT / 2))
        self.velocity = pygame.math.Vector2()
        self.speed = 250

        self.image = pygame.Surface([50, 75])
        self.image.fill(lib.color.white)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.pos += self.velocity * lib.delta_time
        self.rect.center = self.pos

        self.move()

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity.x = -self.speed
        elif keys [pygame.K_d]:
            self.velocity.x = self.speed
        else:
            self.velocity.x = 0

        if keys[pygame.K_w]:
            self.velocity.y = -self.speed
        elif keys[pygame.K_s]:
            self.velocity.y = self.speed
        else:
            self.velocity.y = 0
