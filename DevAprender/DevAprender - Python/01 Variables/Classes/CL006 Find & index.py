# If i want the letter "y"
keyboard = "Keyboard"
print(keyboard[2]) # [index]

newKeyboard = "Keyboard Keyboard Keyboard Keyboard Keyboard KeyboardT"
print(newKeyboard[-1]) # The last index

print(keyboard.index("b"))

# Accessing string's parts (Excluding the last index - [0,5] = [0, 4])
link = "facebook.com/devaprender"
print(link[0]) # First letter
print(link[-1]) # Last letter
print(link[0:5]) # First - Fifth letter
print(link[0:]) # First letter - End
print(link[-5:]) # Last 5 letters
print(link[5:]) # Fifth letter - End
print(link[:-5]) # All -5 letters


# If i want access repeated letters
# C
phrase = "Clean Code"
print(phrase.rindex("C"))
# Or
print(phrase.find("Co"))