#알고리즘을 담아두는 컨테이너 같은 공간.

from util import *
from algo import BruteForce

ALGO_INFO = [
    {
        "name" : "Brute Algo",
        "displacement":(0,FONT_HEIGHT),
        "name_coords" : (0,0),
        "length_coords":(0, HEIGHT + FONT_HEIGHT),
        "depends": -1,
        "sim": BruteForce
    },#모르겠으면 리스트,세부정보를 담아야해->
]

DIVIDERS = [
    (0, HEIGHT + FONT_HEIGHT,WINDOW_WIDTH,HEIGHT+FONT_HEIGHT),
    (WIDTH,0,WIDTH,WINDOW_HEIGHT),
    (WIDTH,0,WIDTH,WINDOW_HEIGHT),
    (WIDTH,0,WIDTH,WINDOW_HEIGHT),
]