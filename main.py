import pygame
import settings
from player import Player
from maze import Maze


def run_game():
    pygame.init()
    window = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Maze Game")

    player = Player()
    maze = Maze()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        # TODO:
        # if maze.is_at_end(player):
        #     maze.generate_new()

        window.fill(settings.BG_COLOR)

        window.fill(settings.BG_COLOR)
        maze.draw(window)
        player.draw(window)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run_game()
