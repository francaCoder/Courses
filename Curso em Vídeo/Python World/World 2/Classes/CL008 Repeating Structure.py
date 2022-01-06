"""
Is for us to do the same thing, but in an easier way
for name in interval()


print("Hello")
print("Hello")
print("Hello")
"""

for c in range(0, 6):
    print("Hello")
print("End")

print(" ")
for c in range(0, 6):
    print(c)
print("End")
print(" ")

for c in range(6, 0, -1): # Reverse
    print(c)
print("End")
print(" ")

for c in range(0, 7, 2): # Jumping 2 by 2
    print(c)
print("End")
print(" ")

n = int(input("Type a number: "))
for c in range(0, n+1):
    print(c)
print("End")
print(" ")

begins = int(input("Starts from: "))
end = int(input("End: "))
jump = int(input("Jumping: "))
for c in range(begins, end+1, jump):
    print(c)
print("End")
print(" ")

for c in range(0, 3):
    n = int(input("Type a value: "))
print("End")
print(" ")

sum = 0
for c in range(0, 4):
    grade = int(input("Put your grade "))
    sum += n
print(sum)