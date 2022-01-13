"""
Create a pro0gram where the user will type an expression with parentheses.
Your code should analyze if the expression are correct or no.
"""

parenthesesRight = parenthesesLeft = 0

expression = str(input("Type an expression: "))
for word in expression:
    for letter in word:
        if letter == "(":
            parenthesesRight += 1
        elif letter == ")":
            parenthesesLeft += 1

if parenthesesRight == parenthesesLeft:
    print("Your expression are correct!")
else:
    print("Your expression are incorrect!")


# OR

expression = str(input("Type an expression: "))
parentheses = []
for letter in expression:
    if letter == "(":
        parentheses.append("(")
    elif letter == ")":
        if len(parentheses) > 0:
            parentheses.pop()
        else:
            parentheses.append(")")
            break
if len(parentheses) == 0:
    print("Your expression are correct!")
else:
    print("Your expression are incorrect!")


# OR

expression = str(input("Type an expression: "))
if expression.count("(") == expression.count(")"):
    print("Your expression are correct!")
else:
    print("Your expression are incorrect!")
