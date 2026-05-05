import pygame, sys, random, math, datetime
from pygame.locals import *
from dataclasses import dataclass, fields
from typing import Optional

# Global Constants

# Set to false for distributions.
DEBUG = True

# Reduce to 30 if performance is very poor.
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
CRIMSON = (100, 5, 5)
SUNSET = (250, 100, 10)

# Global Variables
res_x = 400
res_y = 300

CubeVertices = [
    (0.25, 0.25, 0.25),
    (-0.25, 0.25, 0.25),
    (-0.25, -0.25, 0.25),
    (0.25, -0.25, 0.25),

    (0.25, 0.25, -0.25),
    (-0.25, 0.25, -0.25),
    (-0.25, -0.25, -0.25),
    (0.25, -0.25, -0.25)
    ]

CubeLinks = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

# Functions.

def DebugPoint(point):
    x = point[0]
    y = point[1]
    box_rect = Rect(x-5, y-5, 10, 10)
    pygame.draw.rect(DISPLAYSURF, RED, box_rect)
    return(x,y)

def FixToScreen(x,y):
    x = (x+1)/2*DISPLAYSURF.get_width()
    y = (y+1)/2*DISPLAYSURF.get_height()
    return(x,y)

def Project(point):
    # x = x/z
    x = point[0]/point[2]
    y = point[1]/point[2]
    return(x,y)

def RotatePoint(point, angle):
    x = point[0]
    y = point[1]
    z = point[2]
    c = math.cos(angle)
    s = math.sin(angle)
    x2 = x*c-z*s
    y2 = y
    z2 = x*s+z*c
    return((x2,y2,z2))

def DrawLine(p1, p2):
    pygame.draw.line(DISPLAYSURF, SUNSET, p1, p2, 3)

def RenderPoint(point):
    point = RotatePoint(point, rotation)
    point = (point[0], point[1], point[2]+z)
    return(FixToScreen(*Project(point)))

def DrawFace(face):
    try:
        draw_face = []
        for i in range(0, len(face)):
            draw_face.append(RenderPoint(CubeVertices[face[i]]))
        pygame.draw.polygon(DISPLAYSURF, PURE_WHITE, draw_face)
    except:
        if(DEBUG):
            print("Error rendering model data.")
    

# Setup stuff.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((res_x, res_y), pygame.RESIZABLE)
pygame.display.set_caption("3D Test")
fpsClock = pygame.time.Clock()

z = 1
rotation = 0

while True: # Main game loop - like Unity's "update" void thing.
    rotation += 2*math.pi*(1/TICK_RATE)
    DISPLAYSURF.fill(NIGHT_SKY_BLUE)
    #for point in CubeVertices:
    
    for face in CubeLinks:
        maxthing = len(face)
        for i in range(0, maxthing):
            try:
                p1 = CubeVertices[face[i]]
                p2 = CubeVertices[face[(i+1)%len(face)]]
                p1 = RenderPoint(p1)
                p2 = RenderPoint(p2)
                DrawLine(p1,p2)
            except:
                pass
    
    # This takes a screenshot.
    if(pygame.key.get_pressed()[K_F2]):
        pygame.image.save(DISPLAYSURF, "screenshot.png")

    pygame.display.update()
    fpsClock.tick(TICK_RATE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if(event.key == pygame.key.get_pressed()[K_UP]):
                z += 0.1
                print(z)
            if(event.key == pygame.key.get_pressed()[K_DOWN]):
                z -= 0.1
                print(z)
            if(event.key == pygame.K_COMMA):
                rotation += 10
            if(event.key == pygame.K_PERIOD):
                rotation -= 10