# Create a program that read the width and height of a wall in meters, and calculate
# your area and the amount of ink necessary for painting the wall.
# Considering that each liter of ink paint 2m²

ww = float(input("Wall Width: "))
hw = float(input("Wall Height: "))
area = ww * hw
liters = area / 2

print("With a wall of {} meters of height and {} meters of width, your area is {} "
      "m².".format(hw, ww, area))
print("And you will need {} liters of ink for paint the wall.".format(liters))
