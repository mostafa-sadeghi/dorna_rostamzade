import pygame
import random

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown")

FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
