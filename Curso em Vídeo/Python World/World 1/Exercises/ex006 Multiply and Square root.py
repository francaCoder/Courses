# Create a code that read a number and show in console, the double, triple and square root

n1 = int(input("Type a number: "))
double = n1 * 2
triple = n1 * 3
squareRoot = n1 ** (1/2)

print("The number chosen was {} \nThe double: {} \nTriple: {} \nSquare root: {"
      ":.2f}".format(n1, double, triple, squareRoot))