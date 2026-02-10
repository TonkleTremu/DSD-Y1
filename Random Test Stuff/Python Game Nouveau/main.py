import pygame, sys, random, math
from pygame.locals import *
from dataclasses import dataclass, fields
from typing import Optional


# Global Variables
res_x = 400
res_y = 300

# Global Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
MINT = (61, 255, 171)

# Setup stuff. Should be mostly self-explanatory.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((res_x, res_y), pygame.RESIZABLE)
pygame.display.set_caption("Test")
fpsClock = pygame.time.Clock()
worldSizeX = 100
worldSizeY = 100


@dataclass
class GameObject:
    # The x and y size values. Used for physics-based collisions.
    x_size: float 
    y_size: float
    id: str

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

    # Collision Stuff.
    inCollision: Optional[bool] = False
    collider: Optional[dataclass] = None
    isHeld: Optional[bool] = False

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

    # This code handles velocity.
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
    
    # Moves the picked-up object to the player's centre.
    if(type(player.collider) == type(player)):
        if(player.collider.isHeld):
            player.collider.x = player.x
            player.collider.y = player.y
    
    pygame.draw.circle(DISPLAYSURF, MINT, CoordinatesToScreen(player), 10, 3)

def Rigidbody(Obj: GameObject):
    special_cases = ["player"]
    if(id not in special_cases):
        if(Obj.shape == "box"):
            x,y = CoordinatesToScreen(Obj)
            box_rect = Rect(x, y, Obj.x_size, Obj.y_size)
            pygame.draw.rect(DISPLAYSURF, Obj.color, box_rect)
            pygame.draw.circle(DISPLAYSURF, (255,0,0), (x,y), 1, 1)

def CoordinatesToScreen(Obj):
    '''Converts a GameObject's co-ordinates to a screen location. Takes the GameObject as a parameter.'''
    ScalarX = DISPLAYSURF.get_width() / worldSizeX
    ScalarY = DISPLAYSURF.get_height() / worldSizeY
    x = round(Obj.x * ScalarX)
    y = round(Obj.y * ScalarY)
    return((x,y))

def CompareCoordinates(Obj1, Obj2, allowed_distance):
    point1 = (Obj1.x, Obj1.y)
    point2 = (Obj2.x, Obj2.y)
    if math.dist(point1, point2) < allowed_distance:
        return(True)
    else:
        return(False)

player = GameObject(10, 10, id="player")
box = GameObject(10,10, id="test-box", shape="box", color=MINT, x=50, y=50)
box2 = GameObject(10,10, id="test-box2", shape="box", color=WHITE, x=30, y=30)
GameObjects = [player, box, box2]

while True: # Main game loop - like Unity's "update" void thing.
    DISPLAYSURF.fill(BLACK)

    PlayerMovementHandler()
    for Obj in GameObjects:
        Rigidbody(Obj)
    for Obj1 in GameObjects:
        for Obj2 in GameObjects:
            if(not Obj1 == Obj2):
                if(CompareCoordinates(Obj1, Obj2, Obj1.x_size/2) and Obj1.id == "player" and not Obj1.collider):
                    Obj1.inCollision = True
                    Obj1.collider = Obj2

    pygame.display.update()
    
    # This takes a screenshot.
    if(pygame.key.get_pressed()[K_F2]):
        pygame.image.save(DISPLAYSURF, "screenshot.png")

            
    fpsClock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if(type(player.collider) == type(player)):
                # Grabbing boxes? Lovely!
                if(event.key == pygame.K_g):
                    player.collider.isHeld = not player.collider.isHeld
                    print(player.collider.isHeld)
                    if(not player.collider.isHeld):
                        player.collider = None
                        print(player)