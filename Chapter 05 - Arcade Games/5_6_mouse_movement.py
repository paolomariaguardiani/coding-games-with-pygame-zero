# wiggle your mouse around the screen!

alien = Actor("alien")


def draw():
    screen.clear()
    alien.draw()


def on_mouse_move(pos):  # works also with on_mouse_down
    #     alien.pos = pos
    animate(alien, pos=pos, duration=1, tween="bounce_end")
