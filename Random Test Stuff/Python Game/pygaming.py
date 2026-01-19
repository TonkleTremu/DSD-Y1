import pygame, sys
from pygame.locals import *
from gamelib import *
import random

# Setup stuff. Should be mostly self-explanatory.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((res_x, res_y))
pygame.display.set_caption(game_name)
fpsClock = pygame.time.Clock()

# Dynamic Player Data
player_x = 10
player_y = 10
player_velocity = [0,0]

def PlayerMovementHandler():
    global player_x
    global player_y
    '''Handles player inputs and such.'''
    # Basic movement script. Accepts either WASD or arrow key inputs.
    if(pygame.key.get_pressed()[K_RIGHT] | pygame.key.get_pressed()[K_d]):
        player_x += 1
    if(pygame.key.get_pressed()[K_LEFT] | pygame.key.get_pressed()[K_a]):
        player_x -= 1
    if(pygame.key.get_pressed()[K_UP] | pygame.key.get_pressed()[K_w]):
        player_y -= 1
    if(pygame.key.get_pressed()[K_DOWN] | pygame.key.get_pressed()[K_s]):
        player_y += 1

    # When in wall teleport to other wall.
    if(player_x < PLAYER_WIDTH):
        player_x = res_x - PLAYER_WIDTH
    if(player_x > res_x - PLAYER_WIDTH):
        player_x = 10
    if(player_y < PLAYER_HEIGHT):
        player_y = res_y - PLAYER_HEIGHT
    if(player_y > res_y - PLAYER_HEIGHT):
        player_y = 10

def DrawPattern():
    x = 0
    while(x <= res_x):
        pygame.draw.line(DISPLAYSURF, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (x, res_y), (x+20, res_y))
        x = x+30
    

while True: # Main game loop - like Unity's "update" void thing.
    DISPLAYSURF.fill(WHITE)
    #DrawPattern()
    PlayerMovementHandler()

    pygame.draw.circle(DISPLAYSURF, MINT, (player_x, player_y), 10, 3)
    pygame.display.update()
    fpsClock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()