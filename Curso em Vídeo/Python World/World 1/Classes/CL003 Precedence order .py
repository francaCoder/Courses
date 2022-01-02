# arithmetic operations
# + (add)
# - (subtraction)
# * (Multiply)
# / (Division)
# ** (Potentiation)
# // (whole division)
# % (Module)

# Precedence order
# ()
# ** or pow(n,n)
# * / // %
# + -

# 5 + 3 * 2 == 11
# 3 * 5 + 4 ** 2 == 31
# 3 * (5 + 4) ** 2 == 243

# square root    num ** (1/2)

name = input("What's your name? ")
print("Welcome {:^20}".format(name))
# 20 characters
# < or > or ^ alignment
# :=^20   name in 20 characters in center

# :.3f   3 houseboats

n1 = int(input("A value: "))
n2 = int(input("Other value: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("The sum is {}, the product is {}, the division is {:.3f}".format(s, m, d), end=" ")
# :.3f = 3 houseboats     end=" " don't break line    \n = new line
print("Whole division {} and potency {}".format(di, e))
