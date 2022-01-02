# Create a code that read a value in meters and show in console the same value in
# centimeters and milimeters

meters = float(input("How much meters? "))
cm = meters * 100
mm = meters * 1000

print("{} meters is equal to {:.0f} cm and {:.0f} mm".format(meters, cm, mm))