import pygame
import settings


class Player:
    def __init__(self):
        self.x = 100
        self.y = settings.GROUND_HEIGHT
        self.velocity = 1
        self.width = 20
        self.height = 20

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_UP]:
            self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.y += self.velocity

        # Add vertical movement with gravity here when you implement jumping

    def draw(self, window):
        pygame.draw.rect(
            window, settings.PLAYER_COLOR, (self.x, self.y, self.width, self.height)
        )
