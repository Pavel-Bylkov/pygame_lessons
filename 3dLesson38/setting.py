import math
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH//2
HALF_HEIGHT = HEIGHT//2
FPS = 60
TILE = 50

player_pos = (HALF_WIDTH,HALF_HEIGHT)
player_angle = 0
player_speed = 2

FOV = math.pi/3
HALF_FOV = FOV/2
NUM_RAYS = 60
MAX_DEPTH = 800
DELTA_ANGLE = FOV/NUM_RAYS

DIST = NUM_RAYS/(2*math.tan(HALF_FOV))
PROJ_COEF = 3*DIST * TILE
SCALE = WIDTH//NUM_RAYS


