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

    def break_walls(self, x, y, maze):
        directions = [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2)]
        random.shuffle(directions)
        for nx, ny in directions:
            if 0 <= nx < self.num_columns and 0 <= ny < self.num_rows:
                if not maze[ny][nx]:  # If the cell has not been visited
                    maze[ny][nx] = True
                    maze[ny + (y - ny) // 2][nx + (x - nx) // 2] = True
                    self.break_walls(nx, ny, maze)

    def random_periphery_position(self):
        # Choose a random position on the edges
        if random.choice([True, False]):  # Choose a random horizontal or vertical edge
            x = random.choice([0, self.num_columns - 1])
            y = random.randrange(0, self.num_rows, 2)
        else:
            x = random.randrange(0, self.num_columns, 2)
            y = random.choice([0, self.num_rows - 1])

        return x, y

    def random_starting_position(self, maze):
        # Randomize the starting position
        self.start_x, self.start_y = self.random_periphery_position()
        # If the start is on a border, start carving the maze from a neighboring cell, ensuring there's an entrance
        if self.start_x == 0:
            self.break_walls(self.start_x + 1, self.start_y, maze)
        elif self.start_x == self.num_columns - 1:
            self.break_walls(self.start_x - 1, self.start_y, maze)
        elif self.start_y == 0:
            self.break_walls(self.start_x, self.start_y + 1, maze)
        else:  # self.start_y == self.num_rows - 1
            self.break_walls(self.start_x, self.start_y - 1, maze)

    def ensure_entrance_exit_paths(self, maze):
        # Open path next to the entrance
        if self.start_x == 0:
            if not maze[self.start_y][self.start_x + 1]:
                self.break_walls(self.start_x + 1, self.start_y, maze)
        elif self.start_x == self.num_columns - 1:
            if not maze[self.start_y][self.start_x - 1]:
                self.break_walls(self.start_x - 1, self.start_y, maze)
        elif self.start_y == 0:
            if not maze[self.start_y + 1][self.start_x]:
                self.break_walls(self.start_x, self.start_y + 1, maze)
        else:
            if not maze[self.start_y - 1][self.start_x]:
                self.break_walls(self.start_x, self.start_y - 1, maze)

        # Open path next to the exit (if it is blocked)
        # This should only be done if the exit isn't already on an open path.
        if self.end_x == 0:
            maze[self.end_y][self.end_x + 1] = True
        elif self.end_x == self.num_columns - 1:
            maze[self.end_y][self.end_x - 1] = True
        elif self.end_y == 0:
            maze[self.end_y + 1][self.end_x] = True
        elif self.end_y == self.num_rows - 1:
            maze[self.end_y - 1][self.end_x] = True

    def ensure_borders(self, maze):
        # Add borders around the maze, ensuring the entrance and exit are not blocked
        for x in range(self.num_columns):
            if not (
                (x == self.start_x and 0 == self.start_y)
                or (x == self.end_x and 0 == self.end_y)
            ):
                maze[0][x] = False  # Top border
            if not (
                (x == self.start_x and self.num_rows - 1 == self.start_y)
                or (x == self.end_x and self.num_rows - 1 == self.end_y)
            ):
                maze[self.num_rows - 1][x] = False  # Bottom border

        # Repeat for vertical borders
        for y in range(self.num_rows):
            if not (
                (y == self.start_y and 0 == self.start_x)
                or (y == self.end_y and 0 == self.end_x)
            ):
                maze[y][0] = False  # Left border
            if not (
                (y == self.start_y and self.num_columns - 1 == self.start_x)
                or (y == self.end_y and self.num_columns - 1 == self.end_x)
            ):
                maze[y][self.num_columns - 1] = False  # Right border

    def make_maze(self):
        maze = [[False for _ in range(self.num_columns)] for _ in range(self.num_rows)]

        self.random_starting_position(maze)

        # Mark the starting position as a path
        maze[self.start_y][self.start_x] = True

        # Randomize the ending position, ensuring it's not the same as the start
        self.end_x, self.end_y = self.random_periphery_position()
        while self.start_x == self.end_x and self.start_y == self.end_y:
            self.end_x, self.end_y = self.random_periphery_position()

        # Mark the ending position as a path
        maze[self.end_y][self.end_x] = True

        self.ensure_entrance_exit_paths(maze)

        self.ensure_borders(maze)

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
