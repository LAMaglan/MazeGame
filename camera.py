import pygame


class Camera:
    def __init__(self, width, height, world_width, world_height, zoom_factor=1.0):
        self.width = world_width
        self.height = world_height
        self.zoom_factor = zoom_factor
        zoomed_width = int(width / zoom_factor)
        zoomed_height = int(height / zoom_factor)
        self.camera_rect = pygame.Rect(0, 0, zoomed_width, zoomed_height)

    def apply(self, rect):
        # Offset the rect based on the camera position and zoom factor
        adjusted_rect = pygame.Rect(
            (rect.x - self.camera_rect.x) * self.zoom_factor,
            (rect.y - self.camera_rect.y) * self.zoom_factor,
            rect.width * self.zoom_factor,
            rect.height * self.zoom_factor,
        )
        return adjusted_rect

    def update(self, target):
        # This method centers the zoomed camera on the target (player)
        x = -target.rect.centerx + int(self.camera_rect.width / 2)
        y = -target.rect.centery + int(self.camera_rect.height / 2)

        # Limit scrolling to map size considering the zoom level
        x = min(0, x)  # Left
        y = min(0, y)  # Top
        x = max(-(self.width - self.camera_rect.width), x)  # Right
        y = max(-(self.height - self.camera_rect.height), y)  # Bottom

        self.camera_rect = pygame.Rect(
            x, y, self.camera_rect.width, self.camera_rect.height
        )
