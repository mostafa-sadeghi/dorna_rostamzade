import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
size = (700, 500)
screen = pygame.display.set_mode(size)
# width = screen.get_width()
# height = screen.get_height()
# print(f"width : {width}, height : {height}")
xpos = 0
ypos = 0
change_x_val = 1
change_y_val = 1
clock = pygame.time.Clock()
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = False
            elif event.key == pygame.K_RIGHT:
                xpos += 1
            elif event.key == pygame.K_DOWN:
                ypos += 1

        elif event.type == pygame.QUIT:
            done = False
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [xpos, ypos, 10, 10])
    # xpos += change_x_val
    # ypos += change_y_val

    if ypos > 490 or ypos < 0:
        change_y_val = -1 * change_y_val

    if xpos > 690 or xpos < 0:
        change_x_val = -1 * change_x_val

    pygame.display.flip()
    clock.tick(60)
