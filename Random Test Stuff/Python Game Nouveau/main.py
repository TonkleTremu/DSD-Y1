import pygame, sys, random, math
from pygame.locals import *
from dataclasses import dataclass
from typing import Optional

# Global Variables
res_x = 400
res_y = 300
GameObjects = []

# Global Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
MINT = (61, 255, 171)

# Setup stuff. Should be mostly self-explanatory.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((res_x, res_y))
pygame.display.set_caption("Test")
fpsClock = pygame.time.Clock()


@dataclass
class GameObject:
    # The x and y size values. Used for physics-based collisions.
    x_size: float 
    y_size: float

    # The game object's current co-ordinates.
    x: Optional[float] = 0 
    y: Optional[float] = 0

    color: Optional[tuple] = (0,0,0) # The object's color. Only used if it is a basic algorithmic shape.
    shape: Optional[str] = "circle" # The object's shape. If a sprite is supplied, that will be used instead.
    sprite: Optional[str] = "sprites/error.png" # The object's sprite. If left blank, a shape will be used instead.

    # The values for velocity.
    vel_x: Optional[float] = 0 
    vel_y: Optional[float] = 0
    rot: Optional[float] = 0 # "rot" is the object's rotational speed. Positive = clockwise. 

def PlayerMovementHandler():
    '''Handles player inputs and such.'''
    # Basic movement script. Accepts either WASD or arrow key inputs.
    if(pygame.key.get_pressed()[K_RIGHT] | pygame.key.get_pressed()[K_d]):
        player.x += 1
    if(pygame.key.get_pressed()[K_LEFT] | pygame.key.get_pressed()[K_a]):
        player.x -= 1
    if(pygame.key.get_pressed()[K_UP] | pygame.key.get_pressed()[K_w]):
        player.y -= 1
    if(pygame.key.get_pressed()[K_DOWN] | pygame.key.get_pressed()[K_s]):
        player.y += 1

    # When in wall teleport to other wall.
    if(player.x < player.x_size):
        player.x = res_x - player.x_size
    if(player.x > res_x - player.x_size):
        player.x = player.x_size
    if(player.y < player.y_size):
        player.y = res_y - player.y_size
    if(player.y > res_y - player.y_size):
        player.y = player.y_size
    
    pygame.draw.circle(DISPLAYSURF, MINT, (player.x, player.y), 10, 3)


player = GameObject(10, 10)

while True: # Main game loop - like Unity's "update" void thing.
    DISPLAYSURF.fill(WHITE)

    PlayerMovementHandler()

    pygame.display.update()
    fpsClock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()