"""
Make a program that has a function called area(), that receive the ground's dimensions (width and height) and show the area.
"""


def area(width, height):
    totalArea = (width * height)
    print(f"The ground's area of {width}x{height} is {totalArea}m².")


area(width=float(input("Width (meters): ")), height=float(input("Height (meters): ")))