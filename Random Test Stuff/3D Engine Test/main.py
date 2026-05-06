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
nearclip = -10
debug_mode = False

@dataclass
class GameObject:
    # The xyz size values. Used for physics-based collisions.
    x_size: float 
    y_size: float
    z_size: float

    # The xyz location values.
    x: float
    y: float
    z: float

    # The object's color. By default, it is Sunset.
    color: Optional[tuple] = SUNSET

    # Temporarily stores point data, so the math isn't re-done.
    point_data: Optional[any] = None

CubeLinks = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

# Functions.

def CubeToPoints(cube: GameObject):
    base_cube = [
    (1, 1, 1),
    (0, 1, 1),
    (0, 0, 1),
    (1, 0, 1),

    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 0),
    (1, 0, 0)
    ]
    new_cube = []
    for point in base_cube:
        new_point = (point[0]*cube.x_size+cube.x, point[1]*cube.y_size+cube.y, point[2]*cube.z_size+cube.z)
        new_cube.append(new_point)
    return(new_cube)

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

def DrawLine(p1, p2, color):
    pygame.draw.line(DISPLAYSURF, color, p1, p2, 3)

def RenderPoint(point):
    point = RotatePoint(point, rotation)
    point = (point[0]+x, point[1]+y, point[2]+z)
    if(point[2] < 0):
        return(FixToScreen(*Project(point)))

def DrawFace(face):
    try:
        draw_face = []
        #for i in range(0, len(face)):
            #draw_face.append(RenderPoint(CubeVertices[face[i]]))
        pygame.draw.polygon(DISPLAYSURF, PURE_WHITE, draw_face)
    except:
        if(debug_mode):
            print("Error rendering model data.")

def RenderCube(CubeLinks, CubeVertices, color):
    for face in CubeLinks:
        maxthing = len(face)
        for i in range(0, maxthing):
            try:
                p1 = CubeVertices[face[i]]
                p2 = CubeVertices[face[(i+1)%len(face)]]
                print(p1, z)
                if(p1[2] > z and p2[2] > z):
                    p1 = RenderPoint(p1)
                    p2 = RenderPoint(p2)
                    #if(p1[0] > nearclip and p1[1] > nearclip and p2[0] > nearclip and p2[1] > nearclip):
                    DrawLine(p1,p2, color)
            except:
                pass
    

# Setup stuff.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((res_x, res_y), pygame.RESIZABLE)
pygame.display.set_caption("3D Test")
fpsClock = pygame.time.Clock()

x = 0
y = -1
z = -10
rotation = 0

active_scene = [GameObject(1,1,1,3,3,3), GameObject(0.5,0.5,2,0,-1,3), GameObject(10,15,20,0,1,30)]

while True: # Main game loop - like Unity's "update" void thing.
    rotation += 2*math.pi*(1/TICK_RATE)
    DISPLAYSURF.fill(NIGHT_SKY_BLUE)
    if(debug_mode):
        pygame.draw.line(DISPLAYSURF, RED, (DISPLAYSURF.get_width()/2, 0), (DISPLAYSURF.get_width()/2, DISPLAYSURF.get_height()), 3)
        pygame.draw.line(DISPLAYSURF, RED, (0, DISPLAYSURF.get_height()/2), (DISPLAYSURF.get_width(), DISPLAYSURF.get_height()/2), 3)
    if(pygame.key.get_pressed()[K_UP] | pygame.key.get_pressed()[K_w]):
        z += 0.1
    if(pygame.key.get_pressed()[K_DOWN] | pygame.key.get_pressed()[K_s]):
        z -= 0.1
    if(pygame.key.get_pressed()[K_SPACE]):
        y -= 0.1
    if(pygame.key.get_pressed()[K_LSHIFT]):
        y += 0.1
    if(pygame.key.get_pressed()[K_LEFT] | pygame.key.get_pressed()[K_a]):
        x -= 0.1
    if(pygame.key.get_pressed()[K_RIGHT] | pygame.key.get_pressed()[K_d]):
        x += 0.1
    if(pygame.key.get_pressed()[K_COMMA]):
        rotation -= 10/360
    if(pygame.key.get_pressed()[K_PERIOD]):
        rotation += 10/360
        
    for go in active_scene:
        if(go.point_data == None):
            go.point_data = CubeToPoints(go)
        RenderCube(CubeLinks, go.point_data, go.color)

    pygame.display.update()
    fpsClock.tick(TICK_RATE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if(event.key == pygame.K_F2):
                pygame.image.save(DISPLAYSURF, "screenshot.png")
            if(event.key == pygame.K_F3):
                debug_mode = True
                