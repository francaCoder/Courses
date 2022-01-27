# Create a script that read the name of user, and show a welcome message according the
# value entered

name = input("What's your name?")

print("Nice to meet you {}, welcome.".format(name))

# The kyes, can be used to do the name stay inside them, using '.format()' after string

# Or

name = str(input("What's your name? "))
print(f"Nice to meet you {name}, welcome.")