WIDTH = 500
HEIGHT = 500


alien = Actor("alien")
alien.pos = (400,50)
box = Rect((20,20), (100,100))


def draw():
    screen.clear()
    screen.draw.filled_rect(box, "red")
    alien.draw()


def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2
    if keyboard.up:
        alien.y -= 2
    elif keyboard.down:
        alien.y += 2

    if box.x < alien.x:
        box.x = box.x + 1
    if box.x > alien.x:
        box.x = box.x -1
    if box.y < alien.y:
        box.y += 1
    if box.y > alien.y:
        box.y -= 1
    if alien.colliderect(box):
        exit()
# Write your code here :-)
