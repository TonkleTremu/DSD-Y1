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
worldSizeX = 100
worldSizeY = 100


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
    speed: Optional[float] = 1 # The GameObject's movement speed, used for movement calculations. Higher = faster.
    vel_x: Optional[float] = 0 
    vel_y: Optional[float] = 0

def PlayerMovementHandler():
    '''Handles player inputs and such.'''
    # Basic movement script. Accepts either WASD or arrow key inputs.
    if(pygame.key.get_pressed()[K_RIGHT] | pygame.key.get_pressed()[K_d]):
        player.vel_x += player.speed
    if(pygame.key.get_pressed()[K_LEFT] | pygame.key.get_pressed()[K_a]):
        player.vel_x -= player.speed
    if(pygame.key.get_pressed()[K_UP] | pygame.key.get_pressed()[K_w]):
        player.vel_y -= player.speed
    if(pygame.key.get_pressed()[K_DOWN] | pygame.key.get_pressed()[K_s]):
        player.vel_y += player.speed
    
    acceleration = 15
    deceleration = 15

    if(player.vel_x != 0):
        player.x += player.vel_x / acceleration
        player.vel_x -= player.vel_x / deceleration
        if(player.vel_x < 0.5 and player.vel_x > -0.5):
            player.vel_x = 0
    if(player.vel_y != 0):
        player.y += player.vel_y / acceleration
        player.vel_y -= player.vel_y / deceleration
        if(player.vel_y < 0.5 and player.vel_y > -0.5):
            player.vel_y = 0
        

    # When in wall teleport to other wall.
    BorderX = 0
    BorderY = 0
    if(player.x < BorderX):
        player.x = worldSizeX - BorderX
    if(player.x > worldSizeX - BorderX):
        player.x = BorderX
    if(player.y < BorderY):
        player.y = worldSizeY - BorderY
    if(player.y > worldSizeY - BorderY):
        player.y = BorderY
    
    pygame.draw.circle(DISPLAYSURF, MINT, CoordinatesToScreen(player), 10, 3)

def CoordinatesToScreen(Obj):
    '''Converts a GameObject's co-ordinates to a screen location. Takes the GameObject as a parameter.'''
    ScalarX = DISPLAYSURF.get_width() / worldSizeX
    ScalarY = DISPLAYSURF.get_height() / worldSizeY
    x = round(Obj.x * ScalarX)
    y = round(Obj.y * ScalarY)
    return((x,y))

player = GameObject(10, 10)

while True: # Main game loop - like Unity's "update" void thing.
    DISPLAYSURF.fill(BLACK)

    PlayerMovementHandler()

    pygame.display.update()
    fpsClock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()