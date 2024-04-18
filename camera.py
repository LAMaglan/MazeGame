import pygame


class Camera:
    def __init__(self, width, height, world_width, world_height, zoom_factor=1.0):
        self.width = width
        self.height = height
        self.world_width = world_width
        self.world_height = world_height
        self.zoom_factor = zoom_factor
        self.set_camera_rect(0, 0)

    def set_camera_rect(self, camera_center_x, camera_center_y):
        zoomed_width = int(self.width / self.zoom_factor)
        zoomed_height = int(self.height / self.zoom_factor)
        new_left = camera_center_x - zoomed_width // 2
        new_top = camera_center_y - zoomed_height // 2
        self.camera_rect = pygame.Rect(new_left, new_top, zoomed_width, zoomed_height)

    def apply(self, rect):
        adjusted_x = (rect.x - self.camera_rect.x) * self.zoom_factor
        adjusted_y = (rect.y - self.camera_rect.y) * self.zoom_factor
        adjusted_width = rect.width * self.zoom_factor
        adjusted_height = rect.height * self.zoom_factor

        # Return a new rect with the adjusted position and scaled size
        return pygame.Rect(adjusted_x, adjusted_y, adjusted_width, adjusted_height)

    def update(self, target):
        target_center = target.x + target.width // 2, target.y + target.height // 2
        self.set_camera_rect(*target_center)
