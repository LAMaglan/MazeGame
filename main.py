import pygame
from maze import Maze
from player import Player
import settings

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Instantiate the maze
maze = Maze(settings.MAZE_COLUMNS, settings.MAZE_ROWS, settings.MAZE_CELL_SIZE)

# Instantiate the player at the maze's starting point (passing pixel coordinates)
player = Player(
    start_x=maze.start_x * settings.MAZE_CELL_SIZE + settings.MAZE_CELL_SIZE // 2,
    start_y=maze.start_y * settings.MAZE_CELL_SIZE + settings.MAZE_CELL_SIZE // 2,
    width=settings.PLAYER_WIDTH,
    height=settings.PLAYER_HEIGHT,
)


# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.move(keys, maze)

    # Refresh the screen
    screen.fill((0, 0, 0))  # Clear screen with black

    # Draw the maze
    maze.draw(screen)

    # TODO: mainly for testing purposes
    # Highlight the exit
    exit_rect = pygame.Rect(
        maze.end_x * settings.MAZE_CELL_SIZE,
        maze.end_y * settings.MAZE_CELL_SIZE,
        settings.MAZE_CELL_SIZE,
        settings.MAZE_CELL_SIZE,
    )
    pygame.draw.rect(screen, settings.EXIT_COLOR, exit_rect)

    # Draw the player
    player.draw(screen)

    # Update the display
    pygame.display.flip()

# Cleanup
pygame.quit()
