import turtle
import os


# setup the screen

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()

player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
# everything above sets up the game board

playerSpeed = 15

# Create the enemy

enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemySpeed = 2


def moveLeft():
    x = player.xcor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)


def moveRight():
    x = player.xcor()
    x += playerSpeed
    if x > 280:
        x = 280
    player.setx(x)


# Create keyboard bindings
turtle.listen()
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")


# Main Game loop
while True:

    # Move the enemy
    x = enemy.xcor()
    x += enemySpeed

    enemy.setx(x)

    # Move the enemy back and forth

    if enemy.xcor() > 280:
        enemySpeed *= -1

    if enemy.xcor() < -280:
        enemySpeed *= -1
