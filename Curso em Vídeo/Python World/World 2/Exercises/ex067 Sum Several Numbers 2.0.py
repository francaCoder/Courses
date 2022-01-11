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
print("Finish")