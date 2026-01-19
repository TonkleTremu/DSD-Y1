import pygame, sys
from pygame.locals import *
import random

pygame.init()
res_x = 400
res_y = 300
DISPLAYSURF = pygame.display.set_mode((res_x, res_y))
pygame.display.set_caption('Test Game')

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# Colour Definitions
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player Data
player_height = 10
player_width = 10

player_x = 10
player_y = 10

while True: # main game loop
    DISPLAYSURF.fill(WHITE)

    if(pygame.key.get_pressed()[K_RIGHT]):
        player_x += 1
    if(pygame.key.get_pressed()[K_LEFT]):
        player_x -= 1
    if(pygame.key.get_pressed()[K_UP]):
        player_y -= 1
    if(pygame.key.get_pressed()[K_DOWN]):
        player_y += 1

    # When in wall teleport to other wall.
    if(player_x < player_width):
        player_x = res_x - player_width
    if(player_x > res_x - player_width):
        player_x = 10
    if(player_y < player_height):
        player_y = res_y - player_height
    if(player_y > res_y - player_height):
        player_y = 10
    
    pygame.draw.circle(DISPLAYSURF, BLUE, (player_x, player_y), 10, 3)
    pygame.display.update()
    fpsClock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()