import turtle

# Starting the screen
screen = turtle.Screen()
screen.title("Fractal Tree")
screen.bgcolor("Black")         # Background color

# Starting the turtle
tim = turtle.Turtle()
tim.color("White")              # Color of the tree and turtle
tim.width(1)                    # Tree thickness
tim.speed(10)                   # Speed of turtle

# Upward turtle direction
tim.left(90)

# Recursion function to draw the tree
def draw_tree(i):
    if i < 10:
        return
    else:
        tim.forward(i)
        tim.left(30)
        draw_tree((3*i) / 4)
        tim.right(60)
        draw_tree((3*i) / 4)
        tim.left(30)
        tim.backward(i)


draw_tree(100)             # Number of branches
turtle.mainloop()          # Hold screen
