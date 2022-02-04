from turtle import Turtle
from time import sleep

t = Turtle()

t.speed(1)


def move_forward(turtle):
    pixels = int(input("How many pixels? "))
    while pixels < 1:
        pixels = int(input("Please, how many pixels? (Greater than 0) "))
    print("Moving...")
    sleep(1)
    t.forward(pixels)


def move_backward(turtle):
    pixels = int(input("How many pixels? "))
    while pixels < 1:
        pixels = int(input("Please, how many pixels? (Greater than 0) "))
    print("Moving...")
    sleep(1)
    t.backward(pixels)


def which_direction(turtle):
    direction = str(input("Turn to Left or Right? [L/R] ")).strip().upper()[0]
    while direction not in "LR":
        direction = str(input("Turn to Left or Right? [L/R] ")).strip().upper()[0]
    return direction


def how_many_degrees(turtle):
    angle = int(input("Turn how many degrees: ").strip())
    while angle < 1:
        angle = int(input("Please, type a angle: (Greater than 0) ").strip())
    return angle


def turn_right(turtle):
    t.right(how_many_degrees(t))
    print("Turning...")
    sleep(0.5)


def turn_left(turtle):
    t.left((how_many_degrees(t)))
    print("Turning...")
    sleep(0.5)


while True:
    choice = str(input("Do you want walk or turn? [W/T] ")).strip().upper()[0]
    while choice not in "WT":
        choice = str(input("Do you want walk or turn? [W/T] ")).strip().upper()[0]
    if choice == "W":
        distance = str(input("Move for Forward or Backward? [F/B] ").strip().upper()[0])
        while distance not in "FB":
            distance = str(input("Move for Forward or Backward? [F/B] ").strip().upper()[0])
        if distance == "F":
            move_forward(t)
        if distance == "B":
            move_backward(t)
    elif choice == "T":
        if which_direction(t) == "R":
            turn_right(t)
        else:
            turn_left(t)

