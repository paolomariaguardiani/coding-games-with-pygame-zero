WIDTH = 500
HEIGHT = 500


ball = Rect((150,400), (20,20))
bat = Rect((200, 480), (60, 20))
vx = 4
vy = 4

rectangles = []
for i in range(7):
    rectangles.append(Actor('alien', (i* (WIDTH // 7), 20)))


def draw():
    screen.clear()
    screen.draw.filled_rect(ball, "red")
    screen.draw.filled_rect(bat, "white")
    for rectangle in rectangles:
        rectangle.draw()

def update():
    global vx, vy
    ball.x += vx
    ball.y += vy
    if ball.right > WIDTH or ball.left < 0:
        vx = -vx
    if ball.colliderect(bat) or ball.top < 0:
        vy = -vy
    if ball.bottom > HEIGHT:
        exit()
    if(keyboard.right):
        bat.x += 4
    elif(keyboard.left):
        bat.x -= 4
    for rectangle in rectangles:
        # It must be the rectangle to check collision with ball
        # because rectangle is an actor, while ball is a Rect
        if rectangle.colliderect(ball):
            print("collision!")
            rectangles.remove(rectangle)

