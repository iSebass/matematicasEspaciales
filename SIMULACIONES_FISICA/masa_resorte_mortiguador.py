import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()


#Predefined some colors
BLUE  = (0,0,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

#Screen information
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

while True:
    for event in pygame.event.get():
        if  event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)

    pygame.display.update()
    FramePerSec.tick(FPS)