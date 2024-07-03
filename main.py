import pygame, sys
from define import *

def draw_floor():
    screen.blit(floor, (floor_x_pos, 600))
    screen.blit(floor, (floor_x_pos + WINDOW_WIDTH, 600))
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGH))
clock = pygame.time.Clock()
bg = pygame.transform.scale2x(pygame.image.load(PATH_IMAGE + "bg_5.png")).convert()

floor = pygame.transform.scale2x(pygame.image.load(PATH_IMAGE + "base.png")).convert()

bird = pygame.transform.scale2x(pygame.image.load(PATH_IMAGE + "bird.png")).convert()

bird_rect = bird.get_rect(center = (100, WINDOW_HEIGH/2))
floor_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg, (0, -WINDOW_HEIGH/2))
    screen.blit(bird, bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -WINDOW_WIDTH:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)