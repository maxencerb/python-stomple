import pyglet
from pyglet import shapes
from stomple import Game

nb_player = 4

game = Game(nb_player)

actual_player = 0

board = game.board.board

first = True

window = pyglet.window.Window(1000, 700, caption="Stomple")

def get_player():
    global actual_player
    return actual_player

def next_player():
    global actual_player
    if actual_player == nb_player - 2:
        first = False
    actual_player = (actual_player + 1) % nb_player

def draw_grid():
    batch = pyglet.graphics.Batch()
    back = shapes.Rectangle(0, 0, 7 * w, 7 * w, (42, 157, 236), batch = batch)
    grid = [[
    shapes.Circle(x=i * w + w/2, y=j * w + w/2, radius=w / 2 - 10, color=get_color(board[i,j]), batch=batch) for i in range(7)
    ] for j in range(7)]
    batch.draw()

def draw_players():
    players = pyglet.graphics.Batch()
    player_grid = []
    for player in game.players:
        x, y = player.position
        player_grid.append(shapes.Circle(x=x * w + w/2, y=y * w + w/2, radius=w / 2 - 5, color=(155, 131, 115), batch=players))
        player_grid.append(shapes.Circle(x=x * w + w/2, y=y * w + w/2, radius=w / 2 - 20, color=get_color(player.color), batch=players))
    players.draw()

def draw_label():
    labels = pyglet.graphics.Batch()
    pyglet.text.Label('C\'est au tour de : ', x=750, y=600, color=(255, 255, 255, 255), batch=labels, font_size=20)
    shapes.Circle(x=850, y=500, radius=w/2, color=get_color(actual_player + 1), batch=labels).draw()
    labels.draw()

def get_color(number):
    if number == -1:
        return (0, 0, 0)
    if number == 0:
        # rouge
        return (210, 50, 67)
    if number == 1:
        # noir
        return (90, 90, 90)
    if number == 2:
        # violet
        return (45, 21, 130)
    if number == 3:
        # vert
        return (11, 141, 76)
    if number == 4:
        # orange
        return (240, 94, 32)
    if number == 5:
        # jaune
        return (208, 185, 43)
    else:
        # blanc
        return (255, 255, 255)

w = 100



@window.event
def on_draw():
    window.clear()
    draw_grid()
    draw_players()
    draw_label()

@window.event
def on_close():
    window.close()
    exit()

@window.event
def on_mouse_press(x, y, button, modifiers):
    x, y = int(x/w), int(y/w)
    if 0 <= x < 7 and 0 <= y < 7:
        if not game.players[actual_player].make_move(x, y, first):
            next_player()



pyglet.app.run()
pyglet.clock.schedule_interval(on_draw, 1)

