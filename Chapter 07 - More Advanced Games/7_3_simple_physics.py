WIDTH = 500
HEIGHT = 500


ball = Rect((200, 400), (20, 20))
vx = 10
vy = 10


def draw():
    screen.clear()
    screen.draw.filled_rect(ball, "red")


def update():
    global vx, vy
    ball.x += vx
    ball.y += vy
    if ball.right > WIDTH or ball.left < 0:
#         vx = -vx  # with is the same of vx *= -1
        vx = vx * -1
    if ball.bottom > HEIGHT or ball.top < 0:
        vy = -vy

    # To increase the speed it is important to see every collision
    # with the edge of the window separately;
    # we can't write as before "if ball.right > WIDTH or ball.lfet < 0"
    if ball.right > WIDTH:
        vx -= 0.3
    if ball.left < 0:
        vx += 0.3
    if ball.bottom > HEIGHT:
        vy -= 0.3
    if ball.bottom < 0:
        vy += 0.3

    if vx > 20 or vy > 20:
        vx = 1
        vy = 1

    print(vx, vy)
