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



pygame.mixer.music.play(-1)
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(bg_pic, bg_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
