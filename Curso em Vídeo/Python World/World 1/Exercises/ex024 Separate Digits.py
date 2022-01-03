"""
Make a code that read a number between 0 and 9999 and show on screen each digits.
For exemple: number = 1834
Unity: 4
Ten: 3
Hundred: 8
Thousand: 1

"""
"""
number = (input("Type a number between 0 and 9999: "))
unity = number[3]
ten = number[2]
hundred = number[1]
thousand = number[0]


print("Your Unity is {}".format(unity))
print("Your Ten is {}".format(ten))
print("Your Hundred is {}.".format(hundred))
print("Your Thousand is {}".format(thousand))
"""

number = int(input("Type a number between 0 and 9999: "))
unity = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10


print("Your Unity is {}.".format(unity))
print("Your Ten is {}.".format(ten))
print("Your Hundred is {}.".format(hundred))
print("Your Thousand is {}".format(thousand))

