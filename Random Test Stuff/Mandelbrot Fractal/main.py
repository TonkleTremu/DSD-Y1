import pygame, sys, random, math, datetime
from pygame.locals import *
from dataclasses import dataclass, fields
from typing import Optional

# Global Constants

# Colours
PURE_WHITE = (255,255,255)
PURE_BLACK = (0,0,0)

# Global Variables
res_x = 500
res_y = res_x
timelapse_mode = False

def CheckMandelbrot(point: tuple):
    cx = point[0]
    cy = point[1]
    x = cx
    y = cy
    for i in range(17):
        x = (x*x) - (y*y) + cx
        y = (2*x*y) + (cy)
    if(-1000 < x < 1000 and -1000 < y < 1000):
        return(PURE_BLACK)
    else:
        return(PURE_WHITE)


def GenMandelbrot(zoom: float):
    for ix in range(round(-gridx/2 - zoomx),round(gridx/2 + zoomx)):
        row = []
        for iz in range(round(-gridz/2 - zoomz),round(gridz/2 + zoomz)):
            DISPLAYSURF.set_at((ix+zoomx+round(gridx/2),iz+zoomz+round(gridz/2)), CheckMandelbrot(((ix/(gridx*zoom)),iz/(gridz*zoom))))

# Setup stuff.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((res_x, res_y), RESIZABLE)
pygame.display.set_caption("Fractal")

# Loads and sets fonts.
pygame.font.init()
my_font = pygame.font.SysFont("Agency FB", 30)

images_produced = 0

gridx = DISPLAYSURF.get_width()
gridz = DISPLAYSURF.get_height()

zoom = 0.125
true_zoomx = res_x*2
true_zoomz = 0
zoomx = 0
zoomz = 0

while True: # Main game loop.
    gridx = DISPLAYSURF.get_width()
    gridz = DISPLAYSURF.get_height()

    zoom *= 1.25
    zoomx = round(true_zoomx * zoom)
    zoomz = round(true_zoomz * zoom)

    GenMandelbrot(zoom)
    pygame.display.update()
    pygame.image.save(DISPLAYSURF, f"tempvideofolder/image{images_produced}.jpg")
    images_produced += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if(event.key == pygame.K_F2):
                pygame.image.save(DISPLAYSURF, f"screenshots/screenshot {str(datetime.datetime.now()).replace(":", "")}.png")
                print("Screenshot Saved")
            if(event.key == pygame.K_F3):
                print(f"Zoom: {zoom}")
                