import random

WIDTH = 500
HEIGHT = 500

counter = 0
lista_x_pos = []
lista_y_pos = []

x_pos = 0
y_pos = 0
random_radius = 0

for i in range(10):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    lista_x_pos.append(x)
    lista_y_pos.append(y)

print(lista_x_pos)
print(lista_y_pos)


def draw():
    screen.clear()
    for x in range(0, WIDTH, 40):  # 40 sono gli step
        screen.draw.filled_circle((x, 20), 20, "red")


    for x in range(0, WIDTH, 40):
        for y in range(60, HEIGHT, 40):

            screen.draw.filled_circle((x, y), 10, "green")

    for i in range(10):
        x = lista_x_pos[i]
        y = lista_y_pos[i]
        screen.draw.filled_circle((x, y), 40, "blue")

#     screen.draw.filled_circle((x_pos, y_pos), 20 + random.randint(0, 10), "yellow")  # blinking
    screen.draw.filled_circle((x_pos, y_pos), random_radius, "yellow")


def update():
    global counter, x_pos, y_pos, random_radius
    counter += 1
    if counter > 20:
        x_pos = random.randint(0, WIDTH)
        y_pos = random.randint(0, HEIGHT)
#         random_radius = random.randint(20, 50)
        counter = 0
    random_radius = random.randint(20, 50)  # blinking
