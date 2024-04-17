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

    def break_walls(self, x, y):
        directions = [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2)]
        random.shuffle(directions)
        for nx, ny in directions:
            if 0 <= nx < self.num_columns and 0 <= ny < self.num_rows:
                if not self.maze_grid[ny][nx]:  # If the cell has not been visited
                    self.maze_grid[ny][nx] = True
                    self.maze_grid[ny + (y - ny) // 2][nx + (x - nx) // 2] = True
                    self.break_walls(nx, ny)

    def random_periphery_position(self):
        # Choose a random position on the edges
        if random.choice([True, False]):  # Choose a random horizontal or vertical edge
            x = random.choice([0, self.num_columns - 1])
            y = random.randrange(0, self.num_rows, 2)
        else:
            x = random.randrange(0, self.num_columns, 2)
            y = random.choice([0, self.num_rows - 1])

        return x, y

    def random_starting_position(self):
        # Randomize the starting position
        self.start_x, self.start_y = self.random_periphery_position()
        # If the start is on a border, start carving the self.maze_grid from a neighboring cell, ensuring there's an entrance
        if self.start_x == 0:
            self.break_walls(self.start_x + 1, self.start_y)
        elif self.start_x == self.num_columns - 1:
            self.break_walls(self.start_x - 1, self.start_y)
        elif self.start_y == 0:
            self.break_walls(self.start_x, self.start_y + 1)
        else:  # self.start_y == self.num_rows - 1
            self.break_walls(self.start_x, self.start_y - 1)

    def ensure_entrance_exit_paths(self):
        # Open path next to the entrance
        if self.start_x == 0:
            if not self.maze_grid[self.start_y][self.start_x + 1]:
                self.break_walls(self.start_x + 1, self.start_y)
        elif self.start_x == self.num_columns - 1:
            if not self.maze_grid[self.start_y][self.start_x - 1]:
                self.break_walls(self.start_x - 1, self.start_y)
        elif self.start_y == 0:
            if not self.maze_grid[self.start_y + 1][self.start_x]:
                self.break_walls(self.start_x, self.start_y + 1)
        else:
            if not self.maze_grid[self.start_y - 1][self.start_x]:
                self.break_walls(self.start_x, self.start_y - 1)

        # Open path next to the exit (if it is blocked)
        # This should only be done if the exit isn't already on an open path.
        if self.end_x == 0:
            self.maze_grid[self.end_y][self.end_x + 1] = True
        elif self.end_x == self.num_columns - 1:
            self.maze_grid[self.end_y][self.end_x - 1] = True
        elif self.end_y == 0:
            self.maze_grid[self.end_y + 1][self.end_x] = True
        elif self.end_y == self.num_rows - 1:
            self.maze_grid[self.end_y - 1][self.end_x] = True

    def ensure_borders(self):
        # Add borders around the self.maze_grid, ensuring the entrance and exit are not blocked
        for x in range(self.num_columns):
            if not (
                (x == self.start_x and 0 == self.start_y)
                or (x == self.end_x and 0 == self.end_y)
            ):
                self.maze_grid[0][x] = False  # Top border
            if not (
                (x == self.start_x and self.num_rows - 1 == self.start_y)
                or (x == self.end_x and self.num_rows - 1 == self.end_y)
            ):
                self.maze_grid[self.num_rows - 1][x] = False  # Bottom border

        # Repeat for vertical borders
        for y in range(self.num_rows):
            if not (
                (y == self.start_y and 0 == self.start_x)
                or (y == self.end_y and 0 == self.end_x)
            ):
                self.maze_grid[y][0] = False  # Left border
            if not (
                (y == self.start_y and self.num_columns - 1 == self.start_x)
                or (y == self.end_y and self.num_columns - 1 == self.end_x)
            ):
                self.maze_grid[y][self.num_columns - 1] = False  # Right border

    def add_random_openings(self, num_openings=10, use=True):

        if not use:
            return None

        for _ in range(num_openings):
            # Choose a random wall to open. Avoid the outer walls to maintain the self.maze_grid border.
            wall_x = random.randint(1, self.num_columns - 2)
            wall_y = random.randint(1, self.num_rows - 2)

            # We also ensure that we are only breaking a wall ('False') and not an open path ('True')
            if self.maze_grid[wall_y][wall_x] == False:
                # To avoid making an opening next to another opening, check if neighboring cells are walls
                neighbors = [
                    (wall_x - 1, wall_y),
                    (wall_x + 1, wall_y),
                    (wall_x, wall_y - 1),
                    (wall_x, wall_y + 1),
                ]
                if any(self.maze_grid[ny][nx] == True for nx, ny in neighbors):
                    # Break the wall
                    self.maze_grid[wall_y][wall_x] = True
                else:
                    # Skip this wall, try another one
                    continue

    def make_maze(self):
        self.maze_grid = [
            [False for _ in range(self.num_columns)] for _ in range(self.num_rows)
        ]

        self.random_starting_position()

        # Mark the starting position as a path
        self.maze_grid[self.start_y][self.start_x] = True

        # Randomize the ending position, ensuring it's not the same as the start
        self.end_x, self.end_y = self.random_periphery_position()
        while self.start_x == self.end_x and self.start_y == self.end_y:
            self.end_x, self.end_y = self.random_periphery_position()

        # Mark the ending position as a path
        self.maze_grid[self.end_y][self.end_x] = True

        self.ensure_entrance_exit_paths()

        self.ensure_borders()

        # Add specified number of openings
        self.add_random_openings(num_openings=10, use=True)

        return self.maze_grid

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
        # TODO: Implement logic to check if the player is at the end of the self.maze_grid
        return False

    def generate_new(self):
        # Generate a new self.maze_grid
        selfmaze_grid = self.make_maze()
