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


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    display_surface.blit(system_text,system_text_rect)

    # pygame.draw.line() # exercise  کشیدن خط سفید زیر دو دراگون


    pygame.display.update()

pygame.quit()
