import pygame
import settings


class Player:
    def __init__(self, start_x, start_y, width, height):
        self.x = start_x
        self.y = start_y
        self.velocity = 1
        self.width = width
        self.height = height

    def check_collision(self, dx, dy, maze):
        # Calculate potential new position
        new_x = self.x + dx
        new_y = self.y + dy

        # Find out which cell(s) in the maze grid the player is going to be in after moving
        top_left_cell_x = new_x // maze.cell_size
        top_left_cell_y = new_y // maze.cell_size

        bottom_right_cell_x = (new_x + self.width - 1) // maze.cell_size
        bottom_right_cell_y = (new_y + self.height - 1) // maze.cell_size

        # Get the range of cells that are potentially being intersected
        affected_cells_x = range(top_left_cell_x, bottom_right_cell_x + 1)
        affected_cells_y = range(top_left_cell_y, bottom_right_cell_y + 1)

        # Check all affected cells for collision with walls
        for cell_y in affected_cells_y:
            for cell_x in affected_cells_x:
                # If any of the affected cells are a wall (False), collision detected
                if not maze.maze_grid[cell_y][cell_x]:
                    return True
        return False

    def move(self, keys, maze):
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx = -self.velocity
        if keys[pygame.K_RIGHT]:
            dx = self.velocity
        if keys[pygame.K_UP]:
            dy = -self.velocity
        if keys[pygame.K_DOWN]:
            dy = self.velocity

        new_x = self.x + dx
        new_y = self.y + dy

        # Check collisions for horizontal movement
        if not self.check_collision(dx, 0, maze):
            self.x = new_x
        # Check collisions for vertical movement
        if not self.check_collision(0, dy, maze):
            self.y = new_y

    def draw(self, window):
        pygame.draw.rect(
            window, settings.PLAYER_COLOR, (self.x, self.y, self.width, self.height)
        )
