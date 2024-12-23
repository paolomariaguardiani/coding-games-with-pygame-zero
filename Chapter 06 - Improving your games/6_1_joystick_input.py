import pygame


joystick = pygame.joystick.Joystick(0)
joystick.init()


alien = Actor("alien")
alien.pos = (0, 50)


def draw():
    screen.clear()
    alien.draw()


def update():
    if keyboard.right or joystick.get_axis(0) > 0.7:  # 0.7 = andare più a destra con il joystick
        alien.x = alien.x + 2
    elif keyboard.left or joystick.get_axis(0) < -0.1:
        alien.x = alien.x -2
    if keyboard.up or joystick.get_axis(1) > 0.1:  # > 0.1 vuol dire che stai puntanto in alto
        alien.y += 2
    elif keyboard.down or joystick.get_axis(1) < 0.1:
        alien.y -= 2

