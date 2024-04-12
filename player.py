import pygame
import settings


class Player:
    def __init__(self):
        self.x = settings.PLAYER_START_X
        self.y = settings.PLAYER_START_Y
        self.velocity = 1
        self.width = settings.PLAYER_WIDTH
        self.height = settings.PLAYER_HEIGHT

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_UP]:
            self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.y += self.velocity

    def draw(self, window):
        pygame.draw.rect(
            window, settings.PLAYER_COLOR, (self.x, self.y, self.width, self.height)
        )
