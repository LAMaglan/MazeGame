# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# Player settings
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 10
PLAYER_COLOR = (255, 0, 0)  # Player color

# Constants for the maze dimensions
MAZE_COLUMNS = 50
MAZE_ROWS = 50

# Calculate cell size based on window dimensions and maze layout
MAZE_CELL_SIZE = SCREEN_WIDTH // MAZE_COLUMNS  # This should be an integer result
if SCREEN_HEIGHT // MAZE_ROWS != MAZE_CELL_SIZE:
    raise ValueError(
        "MAZE_CELL_SIZE does not evenly divide WINDOW_HEIGHT and WINDOW_WIDTH. "
        "Adjust MAZE_COLUMNS, MAZE_ROWS, WINDOW_WIDTH, and WINDOW_HEIGHT so they are compatible."
    )


# Colors
BG_COLOR = (0, 0, 0)  # Background color

# TODO: mainly for testing purposes
# RGB color for the exit, green in this case
EXIT_COLOR = (0, 255, 0)
