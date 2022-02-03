"""
Create the turtle mini-game, that allows the user to control which direction the turtle should walk and ask the angle of each move.

Using the turtle mini-game, draw a square according to the instructions given to the turtle.

Initial Tips:
- Create a turtle
- Put your program in a loop
- Ask the user which way the turtle should move.(forward/Backward)
- Then, receive how many pixels
- Ask the user if the turtle should turn left or right
- receive how many pixels
- Ask the user - Do you want to keep walking?
"""



from turtle import Turtle
from time import sleep

t = Turtle()

t.speed(1)

while True:
    choice = str(input("Do you want walk or turn? [W/T] ")).strip().upper()[0]
    while choice not in "WT":
        choice = str(input("Do you want walk or turn? [W/T] ")).strip().upper()[0]
    if choice == "W":
        distance = str(input("Move for Forward or Backward? [F/B] ").strip().upper()[0])
        while distance not in "FB":
            distance = str(input("Move for Forward or Backward? [F/B] ").strip().upper()[0])
        if distance == "F":
            pixels = int(input("How many pixels? "))
            while pixels < 1:
                pixels = int(input("Please, how many pixels? (Greater than 0) "))
                print("Moving...")
                sleep(1)
            t.forward(pixels)
        if distance == "B":
            pixels = int(input("How many pixels? "))
            while pixels < 1:
                pixels = int(input("Please, how many pixels? (Greater than 0) "))
                print("Moving...")
                sleep(1)
            t.backward(pixels)
    if choice == "T":
        direction = str(input("Turn to Left or Right? [L/R] ")).strip().upper()[0]
        while direction not in "LR":
            direction = str(input("Turn to Left or Right? [L/R] ")).strip().upper()[0]
        angle = int(input("Turn how many degrees: ").strip())
        while angle < 1:
            angle = int(input("Please, type a angle: (Greater than 0) ").strip())
        if direction == "L":
            print("Turning...")
            sleep(1)
            t.left(angle)
        if direction == "R":
            print("Turning...")
            sleep(1)
            t.right(angle)
