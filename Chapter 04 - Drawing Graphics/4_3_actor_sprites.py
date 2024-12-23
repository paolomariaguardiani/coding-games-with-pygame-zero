x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x}, {y}'

import pgzrun

width = 500
height = 500

alien = Actor('alien')
alien.x = 0
alien.y = 50


def draw():
    screen.clear()
    alien.draw()


def update():
    alien.x += 2
    if alien.x > width:
        alien.x = 0

pgzrun.go()
