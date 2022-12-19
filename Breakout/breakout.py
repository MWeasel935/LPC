import turtle

# draw screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=500, height=700)
screen.tracer(0)

# draw paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.color("cyan")
paddle.shape("square")
paddle.shapesize(stretch_wid=0.5, stretch_len=2.5)
paddle.penup()
paddle.goto(0, -300)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.penup()
ball.goto(0, -280)
ball.dx = 5
ball.dy = 5


# draw hud
def draw_hud(hud):
    hud.speed(0)
    hud.color("white")
    hud.shape("square")
    hud.penup()
    hud.hideturtle()


score = 0
lifes = 5

score_hud = turtle.Turtle()
draw_hud(score_hud)
score_hud.goto(-100, 300)
score_hud.write("SCORE: {}".format(score), align="center", font=("Agency FB", 24, "bold"))

lifes_hud = turtle.Turtle()
draw_hud(lifes_hud)
lifes_hud.goto(100, 300)
lifes_hud.write("LIFES: {}".format(lifes), align="center", font=("Agency FB", 24, "bold"))


# draw border
border = turtle.Turtle()
draw_hud(border)
border.goto(-255, -350)
border.pendown()
border.width(10)
border.left(90)
border.forward(610)
border.right(90)
border.forward(501)
border.right(90)
border.forward(610)
border.width(10)


# paddle movement
def paddle_left():
    x_pos = paddle.xcor()
    if x_pos > -225:
        x_pos -= 25
    else:
        x_pos = -225
    paddle.setx(x_pos)


def paddle_right():
    x_pos = paddle.xcor()
    if x_pos < 215:
        x_pos += 25
    else:
        x_pos = 215
    paddle.setx(x_pos)


# keyboard binding
screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")

# generate blocks
blocks = []
x, y = -225, 225

for i in range(8):
    for j in range(9):
        block = turtle.Turtle()
        block.speed(0)
        block.shape("square")
        block.shapesize(stretch_wid=0.5, stretch_len=2.5)
        block.penup()
        block.setposition(x, y)
        if i == 0:
            block.color("Red")
        if i == 1:
            block.color("Red")
        if i == 2:
            block.color("Orange")
        if i == 3:
            block.color("Orange")
        if i == 4:
            block.color("Green")
        if i == 5:
            block.color("Green")
        if i == 6:
            block.color("Yellow")
        if i == 7:
            block.color("Yellow")
        blocks.append(block)
        x += 55
    x = -225
    y -= 15


# Ball interactions
def collision():

    # collision with upper wall
    if ball.ycor() >= 250:
        ball.sety(250)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() <= -245:
        ball.setx(-245)
        ball.dx *= -1

    # collision with right wall
    if ball.xcor() >= 235:
        ball.setx(235)
        ball.dx *= -1

    # collision with paddle
    if -300 <= ball.ycor() <= -290:
        if paddle.xcor() + 40 > ball.xcor() > paddle.xcor() - 40:
            ball.sety(-290)
            ball.dy *= -1


# game settings
while True:
    screen.update()
    collision()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    for b in blocks:
        if ball.xcor() + 10 >= b.xcor() - 15 and ball.xcor() - 10 <= b.xcor() + 15:
            if ball.ycor() + 10 >= b.ycor() >= ball.ycor() - 10:
                ball.dy *= -1
                b.goto(1000, 1000)
                score += 1
                score_hud.clear()
                score_hud.write("SCORE: {}".format(score), align="center", font=("Agency FB", 24, "bold"))
                if score == 72:
                    screen.bye()

    if ball.ycor() < -350:
        lifes -= 1
        lifes_hud.clear()
        lifes_hud.write("LIFES: {}".format(lifes), align="center", font=("Agency FB", 24, "bold"))
        ball.dy *= -1
        ball.goto(0, -200)
        if lifes == 0:
            screen.bye()
