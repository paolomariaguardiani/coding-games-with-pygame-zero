WIDTH = 500
HEIGHT = 500
import random


alien = Actor("alien")
alien.pos = (400,50)
box = Rect((20,20),(100,100))
score = 0
background = Actor('background1.png')

def draw():
    screen.clear()
    background.draw()
    screen.draw.filled_rect(box, "green")
    alien.draw()


def update():
    global score
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x -2
    if keyboard.up:
        alien.y -= 2
    elif keyboard.down:
        alien.y += 2

    if alien.colliderect(box):
        box.x = random.randint(0, WIDTH)
        box.y = random.randint(0, HEIGHT)
        score = score + 1
        print("Score: ", score)

