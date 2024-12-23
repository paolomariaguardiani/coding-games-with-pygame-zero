width = 500
height = 500
import random  # my improvment

alien = Actor("alien")
alien.pos = (0, 50)
box = Rect((20,20), (100, 100))


def draw():
    screen.clear()
    screen.draw.filled_rect(box, "red")
    alien.draw()


def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x -= 2
    if keyboard.up:
        alien.y -= 2
    elif keyboard.down:
        alien.y += 2

    box.x += 2
    if box.x > width:
        box.x = 0

    # PLAY SOUND AND SHOW IMAGE WHEN GIT
    if alien.colliderect(box):
        new_y_position = random.randint(0, height)  # my improvment
        box.y = new_y_position
        alien.image = 'alien_hurt'
        sounds.eep.play()
    else:
        alien.image = 'alien'


