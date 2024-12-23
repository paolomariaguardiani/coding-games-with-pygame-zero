alien = Actor("alien")
alien.pos = (0, 50)


def draw():
    screen.clear()
    alien.draw()


def update():
    if keyboard.right or keyboard.d:
        alien.x = alien.x + 2
    elif keyboard.left or keyboard.a:
        alien.x = alien.x - 2
    elif keyboard.up or keyboard.w:
        alien.y = alien.y - 2
    elif keyboard.down or keyboard.s:
        alien.y = alien.y + 2
