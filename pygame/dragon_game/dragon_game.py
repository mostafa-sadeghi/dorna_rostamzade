import random
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
WHITE = (255, 255, 255)

font = pygame.font.Font("AttackGraffiti.ttf", 32)
score_text = font.render(f"Score : {score}", True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (65, 17)

score_image = pygame.image.load("point-icon.png")
score_image_rect = score_image.get_rect()
score_image_rect.topleft = (10, 10)

title_text = font.render("Dragon Game", True, GREEN, DARKGREEN)
title_text_rect = title_text.get_rect()
title_text_rect.centerx = WINDOW_WIDTH / 2
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
game_over_text_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

continue_text = font.render(
    "Press any Key to play again...", True, GREEN, DARKGREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 32)

coin_sound = pygame.mixer.Sound("coin.wav")
miss_sound = pygame.mixer.Sound("sound_1.wav")

background_sound = pygame.mixer.Sound("Bad Piggies Theme.mp3")
background_sound.set_volume(0.3)
background_sound.play(-1)

player_image = pygame.image.load("dragon_right.png")
player_image_rect = player_image.get_rect()
player_image_rect.midleft = (32, WINDOW_HEIGHT / 2 + 20)

coin_image = pygame.image.load("coin.png")
coin_image_rect = coin_image.get_rect()
coin_image_rect.midright = (WINDOW_WIDTH + 50, random.randint(110, WINDOW_HEIGHT - 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_image_rect.top > 75:
        player_image_rect.y -= PLAYER_VELOCITY

    if keys[pygame.K_DOWN] and player_image_rect.bottom < WINDOW_HEIGHT:
        player_image_rect.y += PLAYER_VELOCITY

    if coin_image_rect.x < 0:
        player_lives -= 1
        miss_sound.play()
        coin_image_rect.midright = (WINDOW_WIDTH + 50, random.randint(110, WINDOW_HEIGHT - 50))

    coin_image_rect.x -= coin_velocity

    if player_image_rect.colliderect(coin_image_rect):
        score += 1
        coin_velocity += COIN_ACCELERATION
        coin_sound.play()
        coin_image_rect.midright = (WINDOW_WIDTH + 50, random.randint(110, WINDOW_HEIGHT - 50))

    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_text_rect)
        display_surface.blit(continue_text, continue_text_rect)
        pygame.display.update()
        background_sound.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        background_sound.play(-1)
                        score = 0
                        player_lives = PLAYER_STARTING_LIVES
                        player_image_rect.y = WINDOW_HEIGHT/2
                        coin_velocity = COIN_STARTING_VELOCITY

                        is_paused = False

                    if event.key == pygame.K_ESCAPE:
                        is_paused = False
                        running = False

                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False




    score_text = font.render(f"Score : {score}", True, GREEN, DARKGREEN)
    lives_text = font.render(f"Lives: {player_lives}", True, GREEN, DARKGREEN)

    display_surface.fill(BLACK)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(score_image, score_image_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(heart_image, heart_image_rect)
    display_surface.blit(lives_text, lives_text_rect)

    pygame.draw.line(display_surface, WHITE, (0, 75), (WINDOW_WIDTH, 75), 5)

    display_surface.blit(player_image, player_image_rect)
    display_surface.blit(coin_image, coin_image_rect)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
