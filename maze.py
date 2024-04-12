import random
import pygame
import settings


class Maze:
    def __init__(self):
        self.cell_size = settings.MAZE_CELL_SIZE
        self.num_columns = settings.MAZE_WIDTH
        self.num_rows = settings.MAZE_HEIGHT
        self.maze_grid = self.make_maze()

    def make_maze(self):
        def break_walls(x, y):
            directions = [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2)]
            random.shuffle(directions)
            for nx, ny in directions:
                if 0 <= nx < self.num_columns and 0 <= ny < self.num_rows:
                    if not maze[ny][nx]:  # If the cell has not been visited
                        maze[ny][nx] = True
                        maze[ny + (y - ny) // 2][nx + (x - nx) // 2] = True
                        break_walls(nx, ny)

        maze = [[False for _ in range(self.num_columns)] for _ in range(self.num_rows)]
        start_x, start_y = (settings.PLAYER_START_X, settings.PLAYER_START_Y)
        maze[start_y][start_x] = True

        break_walls(start_x, start_y)

        # Mark the starting cell
        maze[0][1] = True

        # Mark the ending cell
        maze[self.num_rows - 1][self.num_columns - 2] = True

        return maze

    def draw(self, window):
        for y, row in enumerate(self.maze_grid):
            for x, cell in enumerate(row):
                if cell:  # Path
                    color = (255, 255, 255)
                else:  # Wall
                    color = (0, 0, 0)
                pygame.draw.rect(
                    window,
                    color,
                    (
                        x * self.cell_size,
                        y * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )

    def is_at_end(self, player):
        # TODO: Implement logic to check if the player is at the end of the maze
        return False

    def generate_new(self):
        # Generate a new maze
        self.maze_grid = self.make_maze()
