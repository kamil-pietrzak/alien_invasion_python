import sys
import pygame
# import inspect
# src = inspect.getsource(pg)
# print(src)

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Start the main loop for the gameself.
    while True:

        # Watch for keybord and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visable.
        pygame.display.flip()

run_game()
