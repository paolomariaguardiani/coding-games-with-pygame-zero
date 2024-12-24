TITLE = 'Chase Game!!!'
import random

WIDTH = 600
HEIGHT = 600

background = Actor("background")
player = Actor("player")
# player.pos = 200, 200
player.x = 200
player.y = 200

player2 = Actor("alien")
enemy = Actor("enemy_little")
coin = Actor("coin", pos=(300,300))
score = 0
time = 20

game_over = False


def draw():
    screen.clear()
    background.draw()
    player.draw()
    player2.draw()
    coin.draw()
    enemy.draw()

    screen.draw.text("My game", (200, 0), color='red')
    score_string = str(score)
    screen.draw.text("Score: " + score_string, (0,0), color='green', fontsize=50)
    if score == 10:
        screen.draw.text("CONGRATULATIONS!!!", (100, 10), color='green', fontsize=50)

    # time_string = str(round(time))
#     screen.draw.text(time_string, (300, 0), color='green', fontsize = 50)
    screen.draw.text(f"{round(time)}", (300,0), color='green', fontsize = 50)

    if game_over:  # aggiunto da me (based on other tutorial)
        screen.fill("pink")
        screen.draw.textbox("GAME OVER", (0, 200, WIDTH - 20, 200), color="black")


def update(delta):
    global score, time, game_over
    time = time - delta
    if time <= 0:
        game_over = True
    if keyboard.right:
#         per non fargli oltrepassare la finestra
#         if player.x < WIDTH - 32:
#             player.x = player.x + 4
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4

    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y < 0:
        player.y = HEIGHT
    if player.y > HEIGHT:
        player.y = 0

    # Chasing the bee
    if enemy.x < player.x:
        enemy.x = enemy.x + 1
    if enemy.x > player.x:
        enemy.x = enemy.x - 1
    if enemy.y < player.y:
        enemy.y = enemy.y + 1
    if enemy.y > player.y:
        enemy.y = enemy.y - 1
    if player.colliderect(enemy):
#         exit()
        game_over = True

    # collecting coins
    if coin.colliderect(player):
        coin.x = random.randint(0, WIDTH)
        coin.y = random.randint(0, HEIGHT)
        score = score + 1
        time += 2  # I add extra seconds for playing the game

    # moving player2
    if keyboard.d:
        player2.x = player2.x + 4
    if keyboard.a:
        player2.x = player2.x - 4
    if keyboard.s:
        player2.y = player2.y + 4
    if keyboard.w:
        player2.y = player2.y - 4
    if player.colliderect(player2):
        game_over = True


