import turtle
import random

die = [1, 2, 3, 4, 5, 6]

# Starting the screen
screen = turtle.Screen()
screen.title("TURTLE RACING!")

# Starting turtles
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-250, 100)

player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-250, -100)

# Creating turtles homes
player_one.goto(250, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-250, 100)

player_two.goto(250, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-250, -100)

# Settings
for i in range(20):
    if player_one.pos() >= (250, 100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (250, -100):
        print("Player Two Wins!")
        break
    else:
        player_one_turn = input("Press 'Enter' to roll the die (P1): ")
        die_outcome = random.choice(die)
        print(f"The result of the die roll is: {die_outcome}")
        print(f"The number of steps will be: {20*die_outcome}\n")
        player_one.fd(20*die_outcome)

        player_two_turn = input("Press 'Enter' to roll the die (P2): ")
        die_outcome = random.choice(die)
        print(f"The result of the die roll is: {die_outcome}")
        print(f"The number of steps will be: {20 * die_outcome}\n")
        player_two.fd(20*die_outcome)
