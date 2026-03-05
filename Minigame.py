import turtle as trtl
import random as rand

#setup GUI
screen = trtl.Screen()
screen.title("MiniGame")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.listen()

#Create Player
player = trtl.Turtle()
player.shape("circle")
player.color("blue")
player.penup()
player.goto(0,0)

#Make Gun
gun = trtl.Turtle()
gun.shape("circle")
gun.color("red")
gun.speed(10)
gun.penup()
gun.hideturtle()

#moving functions
def move_up():
    y = player.ycor()
    player.sety(y + 20)
    if wall_collision(player):
        player.sety(y)

def move_down():
    y = player.ycor()
    player.sety(y - 20)
    if wall_collision(player):
        player.sety(y)


def move_left():
    x = player.xcor()
    player.setx(x - 20)
    if wall_collision(player):
        player.setx(x)

def move_right():
    x = player.xcor()
    player.setx(x + 20)
    if wall_collision(player):
        player.setx(x)

#Creating Walls

level = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                              X",
    "X                              X",
    "X                              X",
    "X                              X",
    "X                              X",
    "X                              X",
    "X       XXXXXXXXXXXXXXXXX      X",
    "X       X               X      X",
    "X       X               X      X",
    "X       X               X      X",
    "X       X               X      X",
    "X       X               X      X",
    "X       X               X      X",
    "X       X               X      X",
    "X       X               X      X",
    "X       XXXXX       XXXXX      X",
    "X                              X",
    "X                              X",
    "X                              X",
    "X                              X",
    "X                              X",
    "X                              X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

tile_size = 24
walls = []
for y in range(len(level)):
    for x in range(len(level[y])):
        if level[y][x] == "X":
            wall = trtl.Turtle()
            wall.speed(0)
            wall.shape("square")
            wall.color("gray")
            wall.penup()
            wall.goto(
                -380 + x * tile_size,
                280 - y * tile_size
            )
            walls.append(wall)

#Make enemies
enemies = []
def create_enemy():
    enemy = trtl.Turtle()
    enemy.speed(10)
    enemy.shape("circle")
    enemy.color("black")
    enemy.penup()
    enemies.append(enemy)

#wall collision
def wall_collision(player):
    for wall in walls:
        if player.distance(wall) < 20:
            return True
    return False

def wall_collisions(gun):
    for wall in walls:
        if gun.distance(wall) < 20:
            return True
    return False

#Gun Function
def shoot_r():
    gun_y = player.ycor()
    gun_x = player.xcor()
    gun.goto(gun_x, gun_y)
    gun.setheading(0)
    gun.showturtle()
    moving = True
    while moving:
        gun.forward(5)
        for wall in walls:
            if wall_collisions(gun):
                moving = False
                break
    gun.hideturtle()

def shoot_u():
    gun_y = player.ycor()
    gun_x = player.xcor()
    gun.goto(gun_x, gun_y)
    gun.setheading(90)
    gun.showturtle()
    moving = True
    while moving:
        gun.forward(5)
        for wall in walls:
            if wall_collisions(gun):
                moving = False
                break
    gun.hideturtle()    

def shoot_l():
    gun_y = player.ycor()
    gun_x = player.xcor()
    gun.goto(gun_x, gun_y)
    gun.setheading(180)
    gun.showturtle()
    moving = True
    while moving:
        gun.forward(5)
        for wall in walls:
            if wall_collisions(gun):
                moving = False
                break
    gun.hideturtle()

def shoot_d():
    gun_y = player.ycor()
    gun_x = player.xcor()
    gun.goto(gun_x, gun_y)
    gun.setheading(270)
    gun.showturtle()
    moving = True
    while moving:
        gun.forward(5)
        for wall in walls:
            if wall_collisions(gun):
                moving = False
                break
    gun.hideturtle()

#set controls
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(shoot_u, "i")
screen.onkeypress(shoot_d, "k")
screen.onkeypress(shoot_l, "j")
screen.onkeypress(shoot_r, "l")
screen.onkeypress(create_enemy, "z")

trtl.done()