import pygame

import pygame, sys, random, math, datetime
from pygame.locals import *
from dataclasses import dataclass, fields
from typing import Optional


# Global Variables
res_x = 400
res_y = 300

# Global Constants
TICK_RATE = 60

# Colours
PURE_WHITE = (255,255,255)
PURE_BLACK = (0,0,0)
PURE_RED = (255,0,0)
RED = (250,5,5)
GREEN = (5,250,5)
FAUX_GREEN = (5,140,70)
NIGHT_SKY_BLUE = (10,20,140)
LAVENDER = (135,110,170)
BLUE = (5,5,250)
MINT = (61, 255, 171)
GRAY = (124,125,127)
BROWN = (87,54,0)
DELICIOUS_BLUE = (26,251,255)

# Setup stuff. Should be mostly self-explanatory.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((res_x, res_y), pygame.RESIZABLE)
pygame.display.set_caption("Test")
fpsClock = pygame.time.Clock()

def RandomColor():
    returned_color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    return(returned_color)

def GenRandPolygon():
    polygon_sides = random.randint(3, 12)
    points = []
    for x in range(0, polygon_sides):
        points.append((random.randint(0, res_x), random.randint(0, res_y)))
    return(points)

def GenFractalPolygon():
    polygon_sides = 30
    points = []
    prev_x = 90
    for x in range(0, polygon_sides):
        points.append(())
        prev_x = prev_x * math.sin(prev_x)
    print(points)
    return(points)
pygame.draw.polygon(DISPLAYSURF, RandomColor(), points=GenFractalPolygon())
while True: # Main game loop - like Unity's "update" void thing.
    #DISPLAYSURF.fill(NIGHT_SKY_BLUE)
    #pygame.draw.polygon(DISPLAYSURF, RandomColor(), points=GenRandPolygon())

    pygame.display.update()
    
    # This takes a screenshot.
    if(pygame.key.get_pressed()[K_F2]):
        pygame.image.save(DISPLAYSURF, "screenshot.png")

            
    fpsClock.tick(TICK_RATE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()