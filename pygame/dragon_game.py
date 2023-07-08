import pygame


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dragon Game")


FPS = 60
clock = pygame.time.Clock()

PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5


score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

GREEN = (14, 158, 53)
DARKGREEN = (21, 121, 46)
CUSTOMWHITE = (183, 206, 205)
BLACK = (0, 0, 0)


font = pygame.font.Font("AttackGraffiti.ttf", 32)
score_text = font.render(f"Score : {score}", True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (65, 17)


score_image = pygame.image.load("point-icon.png")
score_image_rect = score_image.get_rect()
score_image_rect.topleft = (10, 10)


title_text = font.render("Dragon Game", True, GREEN, DARKGREEN)
title_text_rect = title_text.get_rect()
title_text_rect.centerx = WINDOW_WIDTH/2
title_text_rect.y = 17

lives_text = font.render(f"Lives: {player_lives}", True, GREEN, DARKGREEN)
lives_text_rect = lives_text.get_rect()
lives_text_rect.centerx = WINDOW_WIDTH - 110
lives_text_rect.y = 17


heart_image = pygame.image.load("Heart-icon.png")
heart_image_rect = heart_image.get_rect()
heart_image_rect.topright = (WINDOW_WIDTH, 10)


game_over_text = font.render("GameOver", True, GREEN, DARKGREEN)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

continue_text = font.render(
    "Press any Key to play again", True, GREEN, DARKGREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 32)


coin_sound = pygame.mixer.Sound("coin.wav")
miss_sound = pygame.mixer.Sound("sound_1.wav")

pygame.mixer.music.load("music.wav")


# TODO load player image


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(score_text, score_rect)
    display_surface.blit(score_image, score_image_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(heart_image, heart_image_rect)
    display_surface.blit(lives_text, lives_text_rect)

    pygame.display.update()

    clock.tick(FPS)


pygame.quit()
