import random
import pygame


class Maze:
    def __init__(self, num_columns, num_rows, cell_size):
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.cell_size = cell_size

        self.start_x, self.start_y = 0, 0
        self.end_x, self.end_y = 0, 0
        self.maze_grid = self.make_maze()

    def random_periphery_position(self):
        # Choose a random position on the edges
        if random.choice([True, False]):  # Choose a random horizontal or vertical edge
            x = random.choice([0, self.num_columns - 1])
            y = random.randrange(0, self.num_rows, 2)
        else:
            x = random.randrange(0, self.num_columns, 2)
            y = random.choice([0, self.num_rows - 1])

        return x, y

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

        # Randomize the starting position
        self.start_x, self.start_y = self.random_periphery_position()
        # If the start is on a border, start carving the maze from a neighboring cell, ensuring there's an entrance
        if self.start_x == 0:
            break_walls(self.start_x + 1, self.start_y)
        elif self.start_x == self.num_columns - 1:
            break_walls(self.start_x - 1, self.start_y)
        elif self.start_y == 0:
            break_walls(self.start_x, self.start_y + 1)
        else:  # self.start_y == self.num_rows - 1
            break_walls(self.start_x, self.start_y - 1)

        # Mark the starting position as a path
        maze[self.start_y][self.start_x] = True

        # Randomize the ending position, ensuring it's not the same as the start
        self.end_x, self.end_y = self.random_periphery_position()
        while self.start_x == self.end_x and self.start_y == self.end_y:
            self.end_x, self.end_y = self.random_periphery_position()

        # Mark the ending position as a path
        maze[self.end_y][self.end_x] = True

        return maze

    def draw(self, window):
        for y, row in enumerate(self.maze_grid):
            for x, cell in enumerate(row):
                if cell:
                    color = (255, 255, 255)  # Cell open
                else:
                    color = (0, 0, 0)  # Cell blocked
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
