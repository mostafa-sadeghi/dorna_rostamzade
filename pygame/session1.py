# pip install arabic-reshaper
# pip install python-bidi


import pygame
import arabic_reshaper
from bidi.algorithm import get_display
pygame.init()


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Our First Game")

GREEN = (0,255,0)# RGB
DARKGREEN = (10,50,10)# RGB
BLACK = (0,0,0)# RGB
WHITE = (255,255,255)# RGB

# sound_1 = pygame.mixer.Sound('sound_1.wav')
# sound_1.play()
# pygame.time.delay(500)
# sound_2 = pygame.mixer.Sound('sound_2.wav')
# sound_2.play()
# pygame.time.delay(500)

# sound_2.set_volume(0.1)
# sound_2.play()

pygame.mixer.music.load('music.wav')

pygame.mixer.music.play(-1,0.0)
# pygame.time.delay(3000)
# pygame.mixer.music.stop()

fonts = pygame.font.get_fonts()
# for font in fonts:
#     print(font)
system_font = pygame.font.SysFont('sahelblack',64)
custom_font = pygame.font.Font('AttackGraffiti.ttf', 32)

text_to_be_reshaped = 'بازی دراگون'
reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
bidi_text = get_display(reshaped_text)
system_text = system_font.render(bidi_text, True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# custom_text :  "Move the dragon soon"

# در وسط صفحه کمی پایین تر از متن فارسی قبلی



dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)


dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)



dragon_image = pygame.image.load('dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH//2
dragon_rect.bottom = WINDOW_HEIGHT



VELOCITY = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY

    display_surface.fill(BLACK)
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    pygame.draw.line(display_surface, WHITE, (0,75), (WINDOW_WIDTH, 75), 4)
    # display_surface.blit(system_text,system_text_rect)
    display_surface.blit(dragon_image,dragon_rect)
    # pygame.draw.line() # exercise  کشیدن خط سفید زیر دو دراگون


    pygame.display.update()

pygame.quit()
