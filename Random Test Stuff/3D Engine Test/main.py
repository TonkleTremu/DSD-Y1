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

# Global Variables
res_x = 400
res_y = 300

# "Display Surface" - this is where all the stuff is rendered to. 
DISPLAYSURF = pygame.display.set_mode((res_x, res_y), pygame.RESIZABLE)

@dataclass
class GameObject:
    # The x and y size values. Used for physics-based collisions.
    size: tuple
    position: Optional[tuple]
    color: Optional[tuple] = PURE_WHITE