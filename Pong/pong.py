import turtle

# draw screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


# draw paddles
def draw_paddle(paddle, x):
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, 0)


paddle_1 = turtle.Turtle()
draw_paddle(paddle_1, -350)

paddle_2 = turtle.Turtle()
draw_paddle(paddle_2, 350)


# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Agency FB", 24, "bold"))


def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 25
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -25
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 25
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -25
    else:
        y = -250
    paddle_2.sety(y)


# binding
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")


def interact():
    # collision with the upper wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # collision with the paddle 1
    if -360 <= ball.xcor() <= -330:
        if paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
            ball.setx(-330)
            ball.dx *= -1

    # collision with the paddle 2
    if 360 >= ball.xcor() >= 330:
        if paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
            ball.setx(330)
            ball.dx *= -1


score_1 = 0
score_2 = 0


def set_score():
    global score_1, score_2

    # collision with left wall
    if ball.xcor() < -390:
        score_2 += 1
        ball.goto(0, 0)
        ball.dx *= -1

    # collision with right wall
    if ball.xcor() > 390:
        score_1 += 1
        ball.goto(0, 0)
        ball.dx *= -1

    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Agency FB", 24, "bold"))


while True:
    screen.update()
    interact()
    set_score()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
