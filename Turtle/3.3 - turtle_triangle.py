import turtle

# Starting the screen
screen = turtle.Screen()
screen.title("Draw a trinagle")
screen.bgcolor("Black")         # Background color

# Starting the turtle
tim = turtle.Turtle()
tim.color("White")              # Color of the tree and turtle
tim.width(1)                    # Tree thickness
tim.speed(3)                    # Speed of turtle


# Function to draw a triangle in cursor position
def draw_triangle(x, y):
    tim.penup()
    tim.goto(x, y)
    tim.pendown()
    for i in range(3):
        tim.forward(100)
        tim.left(120)


turtle.onscreenclick(draw_triangle, 1)

turtle.listen()

turtle.mainloop()
