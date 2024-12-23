timer = 5

def update(dt):
    global timer
    timer -= dt


def draw():
    screen.clear()
    screen.draw.text(f"time passed: {timer}", (0,0))
    if timer < 0:
        screen.draw.textbox("Time's up!", Rect(50,50,200,200))

