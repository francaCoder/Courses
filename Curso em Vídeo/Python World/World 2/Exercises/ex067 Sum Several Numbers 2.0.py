"""
Make a code that read several whole numbers. The stop condition is 999.
at the end show how many numbers was typed and the sum among them.
(Disregarding the flag)
"""

sum = numbers = 0
while True:
    num = int(input("Type a number (999 to stop) "))
    if num == 999:
        break
    sum += num
    numbers += 1

print(" ")
print("The numbers sum is {} and you typed {} numbers.".format(sum, numbers))
print("Finish")