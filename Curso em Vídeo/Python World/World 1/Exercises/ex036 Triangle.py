# Make a code that read 3 line measurements and say if it's possible make a triangle

s1 = float(input("First Straight: "))
s2 = float(input("Second Straight: "))
s3 = float(input("Third Straight: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("The straights above can form a triangle.")
else:
    print("The straights below can't form a triangle.")
