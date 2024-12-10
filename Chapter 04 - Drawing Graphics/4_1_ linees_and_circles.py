x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x}, {y}'

import pgzrun

WIDTH = 600
HEIGHT = 600

def draw():
    screen.clear()
    screen.draw.filled_circle((250,100), 50, "red")
    screen.draw.circle((250,250), 50, "white")
    screen.draw.circle((250,400), 50, "white")
    screen.draw.line((150,20), (150,500), "purple")
    screen.draw.line((150,20), (350,20), "purple")
    screen.draw.line((350,20), (350, 500), "purple")
    screen.draw.line((150,500), (350,500), "purple")
    



pgzrun.go()