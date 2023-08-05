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


bg_pic = pygame.image.load("background.png")
bg_rect = bg_pic.get_rect()
bg_rect.topleft = (0, 0)


clown_image = pygame.image.load("clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

score = 0
player_lives = 5
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)
RED = (255, 0, 0)

font = pygame.font.Font("Franxurter.ttf", 48)

title_text = font.render("Catch The Clown", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render(f"Score: {score}", True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render(f"Lives: {player_lives}", True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

pygame.mixer.music.load("ctc_background_music.wav")
click_sound = pygame.mixer.Sound("click_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")

clown_dx = random.choice((-1,1))
clown_dy = random.choice((-1,1))
clown_velocity = 5
pygame.mixer.music.play(-1)
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
          
            if clown_rect.collidepoint(event.pos):
                click_sound.play()
                score += 1
                clown_velocity += 1

            else:
                miss_sound.play()
                player_lives -= 1


    clown_rect.x += clown_dx * clown_velocity
    clown_rect.y += clown_dy * clown_velocity

    if clown_rect.bottom > WINDOW_HEIGHT or clown_rect.top < 0:
        clown_dy = -1 * clown_dy
    if clown_rect.right > WINDOW_WIDTH or clown_rect.left < 0:
        clown_dx *= -1

    score_text = font.render(f"Score: {score}", True, YELLOW)
    lives_text = font.render(f"Lives: {player_lives}", True, YELLOW)

    display_surface.blit(bg_pic, bg_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(clown_image, clown_rect)
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
