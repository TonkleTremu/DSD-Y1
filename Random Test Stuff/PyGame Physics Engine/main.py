import pygame, sys, random, math, datetime
from pygame.locals import *
from dataclasses import dataclass, fields
from typing import Optional
from physicslib import *


# Global Variables
res_x = 400
res_y = 300

# Global Constants
TICK_RATE = 60

# Setup stuff. Should be mostly self-explanatory.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((res_x, res_y), pygame.RESIZABLE)
pygame.display.set_caption("Test")
fpsClock = pygame.time.Clock()
worldSizeX = 100
worldSizeY = 100
player = GameObject(10, 10, id="player")
box = GameObject(10,10, id="test-box", shape="box", color=MINT, x=50, y=50)
box2 = GameObject(10,10, id="test-box2", shape="box", color=DELICIOUS_BLUE, x=30, y=30)
GameObjects = [player, box, box2]
Boxes = [box,box2]

while True: # Main game loop - like Unity's "update" void thing.
    DISPLAYSURF.fill(NIGHT_SKY_BLUE)

    PlayerMovementHandler()
    random.shuffle(GameObjects)
    for Obj in GameObjects:
        Rigidbody(Obj)
        try:
            if(not(CompareCoordinates(Obj, Obj.collider, Obj.x_size/2))):
                Obj.collider = None
        except:
            pass
    for Obj1 in GameObjects:
        for Obj2 in GameObjects:
            if(not Obj1 == Obj2):
                if(CompareCoordinates(Obj1, Obj2, Obj1.x_size/2) and Obj1.id == "player"):
                    Obj1.collider = Obj2
    for box in Boxes:
        SnapToGrid(box)

    pygame.display.update()
    
    # This takes a screenshot.
    if(pygame.key.get_pressed()[K_F2]):
        pygame.image.save(DISPLAYSURF, "screenshot.png")

            
    fpsClock.tick(TICK_RATE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Grabbing boxes? Lovely!
            if(event.key == pygame.K_g):
                if(player.holding == None):
                    player.holding = player.collider
                else:
                   player.holding = None
            # Provides various debug information.
            if(event.key == pygame.K_z):
                WriteLog()