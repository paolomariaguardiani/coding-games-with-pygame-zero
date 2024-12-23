x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x}, {y}'

import pgzrun
width = 500
height = 500

box1 = Rect((20, 20), (50, 50))
box2 = Rect((420,420), (450, 450))

def draw():
    screen.clear()
    screen.draw.filled_rect(box1, "red")
    screen.draw.filled_rect(box2, "green")


def update():
    box1.x = box1.x + 2
    if box1.x > width:
        box1.x = 0
    box2.x = box2.x - 3
    if box2.x < 0:
        box2.x = 450




pgzrun.go()