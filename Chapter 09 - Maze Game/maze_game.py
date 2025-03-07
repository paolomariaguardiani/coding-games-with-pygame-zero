import pgzrun

TITLE = "Maze Game"

TILE_SIZE = 64
WIDTH = TILE_SIZE * 8
HEIGHT = TILE_SIZE * 8


tiles = ["empty", "wall", "goal", "door", "key"]
unlock = 0


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 2, 0, 1],
    [1, 0, 1, 0, 1, 1, 3, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 4, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

player = Actor("bee", anchor=(0, 0), pos=(1 * TILE_SIZE, 6 * TILE_SIZE))
enemy = Actor("enemy", anchor=(0,0), pos= (3 * TILE_SIZE, 6 *TILE_SIZE))
enemy.yv = -1


def draw():
    screen.clear()
    # We design the map (thanks to CODING MAGES WITH PYGAME ZERO & PYTHON)
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles[maze[row][column]]
            screen.blit(tile, (x, y))
    player.draw()
    enemy.draw()


def on_key_down(key):
    row = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)
    if key == keys.UP:
        row = row - 1
    if key == keys.DOWN:
        row = row + 1
    if key == keys.LEFT:
        column = column -1
    if key == keys.RIGHT:
        column = column + 1
    # player.x = column * TILE_SIZE
#     player.y = row * TILE_SIZE
#     print(row, column, player.x, player.y)
    tile = tiles[maze[row][column]]
    if tile == 'empty':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration = 0.1, pos = (x, y))
            # player.x = column * TILE_SIZE
#             player.y = row * TILE_SIZE
#          elif tile == 'goal':
#             print("Well done")
#             exit()
    global unlock
    if tile == 'goal':
        print("Well done")
        # exit()
    elif tile == 'key':
        unlock = unlock + 1
        maze[row][column] = 0# 0 is 'empty' tile
    elif tile == 'door' and unlock > 0:
        unlock = unlock -1
        maze[row][column] = 0 # 0 is 'empty' tile

    # enemy movement
    row = int(enemy.y / TILE_SIZE)
    column = int(enemy.x / TILE_SIZE)
    row = row + enemy.yv
    tile = tiles[maze[row][column]]
    if not tile == 'wall':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(enemy, duration=0.1, pos=(x,y))
    else:
        enemy.yv = enemy.yv * -1
#         enemy.yv = -enemy.yv
    if enemy.colliderect(player):
        print("You died")
        exit()

# This is my versione of the previous funcion
# def on_key_down(key):
#     if key == keys.UP:
#         player.y -= TILE_SIZE
#     if key == keys.DOWN:
#         player.y += TILE_SIZE
#     if key == keys.LEFT:
#         player.x -= TILE_SIZE
#     if key == keys.RIGHT:
#         player.x += TILE_SIZE


pgzrun.go()
