import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
# set the width and height of the screen [width,height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Snow animation")
# Loop until the user clicks the close button.
done = True
clock = pygame.time.Clock()

snow_list = []
for i in range(50):
    x = random.randrange(0, 500)
    y = random.randrange(0, 700)
    snow_list.append([x, y])


# Main Program Loop
while done:  # main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    # Game logic should go here

    # Screen clearing code goes here
    screen.fill(BLACK)

    # Drawing code shuld go here
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1

        if snow_list[i][1] > 500:
            snow_list[i][1] = random.randrange(-50, -10)
            snow_list[i][0] = random.randrange(700)
    # go ahead and update the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
