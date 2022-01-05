"""
Redo the 'ex036 Triangle' exercise adding a new function, what's type of triangle can be
formed?

equilateral: All equal sides
isosceles: Two equal sides
scalene triangle: All different sides
"""

s1 = float(input("First Straight: "))
s2 = float(input("Second Straight: "))
s3 = float(input("Third Straight: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("The straights above can form a triangle.")
else:
    print("The straights below can't form a triangle.")
