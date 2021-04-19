
#Imports
import pygame as pg
import random as rd
import sys
import math
from pygame.math import Vector2 as vec

###SETTING VARIABLES
WIDTH = 960
HEIGHT = 544


disp = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Slimes Attack")
pg.init()

CROSSBOWDAMAGE = 5
TRIPLECROSSBOWDAMAGE = 5
GREENSLIMEHEALTH = 15
BLUESLIMEHEALTH = 30
AMMOBARWIDTH = 50

ENEMYMULTIPLIER = 3
DELAYMULTIPLIER = 10
INBETWEENDELAY = 1.5

FONT = "FiddlersCoveBold-7JJV.otf"


GAMEOVERTEXTPOSITIONS = [[11*32,1*32],[12*32,5*32],[12*32,7*32],[6*32,14*32],[19*32,14*32]]
WAVETEXTPOSITION = [1*32,15*32]
SCORETEXTPOSITION = [14*32,0*32]

SLIMESCORES = [5,10,20]

###LOADING IMAGES






###LOADING AUDIO





#####COLORS
BLACK = (0,0,0)