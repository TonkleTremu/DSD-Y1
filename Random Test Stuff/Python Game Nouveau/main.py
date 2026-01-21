import pygame, sys, random, math
from pygame.locals import *

# Global Variables
res_x = 400
res_y = 300
GameObjects = []

# Global Constants
WHITE = (255,255,255)
BLACK = (0,0,0)

# Setup stuff. Should be mostly self-explanatory.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test")
fpsClock = pygame.time.Clock()

class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def ShowGameObjects():
    for Object in GameObjects:
        pygame.draw.circle(DISPLAYSURF, BLACK, (Object.x, Object.y), 10, 1)

player = GameObject(20, 20, 5, 5)

while True: # Main game loop - like Unity's "update" void thing.
    DISPLAYSURF.fill(WHITE)

    ShowGameObjects()

    pygame.display.update()
    fpsClock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()