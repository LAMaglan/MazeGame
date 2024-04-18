import pygame


class Camera:
    def __init__(self, width, height, world_width, world_height):
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.width = world_width
        self.height = world_height

    def apply(self, rect):
        # take self.rect from player (based on pygame.Rect)
        return rect.move(-self.camera_rect.x, -self.camera_rect.y)

    def update(self, target):
        # This method centers the camera on the target (player)
        x = -target.rect.centerx + int(self.camera_rect.width / 2)
        y = -target.rect.centery + int(self.camera_rect.height / 2)

        # Limit scrolling to map size
        x = min(0, x)  # Left
        y = min(0, y)  # Top
        x = max(-(self.width - self.camera_rect.width), x)  # Right
        y = max(-(self.height - self.camera_rect.height), y)  # Bottom

        self.camera_rect = pygame.Rect(
            x, y, self.camera_rect.width, self.camera_rect.height
        )
