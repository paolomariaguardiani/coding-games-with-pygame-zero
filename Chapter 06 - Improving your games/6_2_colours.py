# my_colour = (0,0,0) # makes black
# my_colour = (255,255,255) # makes white
import random

red_amount = 0
green_amount = 0
blue_amount = 0
counter = 0

def draw():
    my_colour = (red_amount, green_amount, blue_amount)
    screen.fill(my_colour)


# This function makes the colour change every frame
# Remove it if you just want to see a static color.
def update():
    global red_amount, green_amount, blue_amount, counter
    red_amount += 1
    counter += 1
    red_amount = red_amount % 255  # con questo trucchetto non superi mai il numero 255
    if counter == 60:
        green_amount = random.randint(0, 255)  # cambia il livello di colore verde ogni secondo
        blue_amount = random.randint(0, 255)
        counter = 0

    print(red_amount, green_amount, blue_amount)
