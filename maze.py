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
        edge = random.choice(["top", "bottom", "left", "right"])
        if edge == "top":
            x = random.randrange(2, self.num_columns - 3, 2)
            y = 2
        elif edge == "bottom":
            x = random.randrange(2, self.num_columns - 3, 2)
            y = self.num_rows - 3
        elif edge == "left":
            x = 2
            y = random.randrange(2, self.num_rows - 3, 2)
        else:  # 'right'
            x = self.num_columns - 3
            y = random.randrange(2, self.num_rows - 3, 2)

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

        # Initialize the maze as a grid of False (walls)
        maze = [[False for _ in range(self.num_columns)] for _ in range(self.num_rows)]

        # Randomize the starting and ending positions
        self.start_x, self.start_y = self.random_periphery_position()
        self.end_x, self.end_y = self.random_periphery_position()
        while self.start_x == self.end_x and self.start_y == self.end_y:
            self.end_x, self.end_y = self.random_periphery_position()

        # Carve out the path starting from a cell adjacent to the starting position
        if self.start_x == 2:  # If it's on the left edge
            maze[self.start_y][self.start_x - 1] = True
            break_walls(self.start_x + 2, self.start_y)
        elif self.start_x == self.num_columns - 3:  # If it's on the right edge
            maze[self.start_y][self.start_x + 1] = True
            break_walls(self.start_x - 2, self.start_y)
        elif self.start_y == 2:  # If it's on the top edge
            maze[self.start_y - 1][self.start_x] = True
            break_walls(self.start_x, self.start_y + 2)
        elif self.start_y == self.num_rows - 3:  # If it's on the bottom edge
            maze[self.start_y + 1][self.start_x] = True
            break_walls(self.start_x, self.start_y - 2)

        # Carve out the path for the exit
        if self.end_x == 2:
            # Left edge, ensure we're not replacing the start
            if maze[self.end_y][self.end_x - 1] == False:
                maze[self.end_y][self.end_x - 1] = True
        elif self.end_x == self.num_columns - 3:
            # Right edge, ensure we're not replacing the start
            if maze[self.end_y][self.end_x + 1] == False:
                maze[self.end_y][self.end_x + 1] = True
        elif self.end_y == 2:
            # Top edge, ensure we're not replacing the start
            if maze[self.end_y - 1][self.end_x] == False:
                maze[self.end_y - 1][self.end_x] = True
        elif self.end_y == self.num_rows - 3:
            # Bottom edge, ensure we're not replacing the start
            if maze[self.end_y + 1][self.end_x] == False:
                maze[self.end_y + 1][self.end_x] = True

        maze[self.start_y][self.start_x] = True  # Ensure the start is open
        maze[self.end_y][self.end_x] = True  # Ensure the end is open

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
