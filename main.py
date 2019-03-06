import turtle
import os
import math

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

# Create the players ammo

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 20

# Define bullet state
# ready -> ready to fire
# Fire -> bullet is moving

bulletState = "ready"


def fireBullet():
    # Declare bulletstate as a global
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        # Move Bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) +
                         math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


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
turtle.onkey(fireBullet, "space")


# Main Game loop
while True:

    # Move the enemy
    x = enemy.xcor()
    x += enemySpeed

    enemy.setx(x)

    # Move the enemy back and forth
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemySpeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemySpeed *= -1
        enemy.sety(y)

    # Move the bullet
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

    # Check to see if bullet is gone
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"

    # Check for bullet collision with the enemy
    if isCollision(bullet, enemy):
        bullet.hideturtle()
        bulletState = "ready"
        bullet.setposition(0, -400)
        # reset the enemy
        enemy.setposition(-200, 250)

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break
