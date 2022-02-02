# If we need join or split words: join() and split()
phrase = "Hello, welcome-to python!"
print(phrase.split()) # A  list with each word
print(phrase.split(",")) # Split in ,
print(phrase.split("-"))

names = "Matheus, Maria, João, Carlos"
print(names.split(","))

hashtags = "music #guitar #gamer #coder #python"
print(hashtags.split("#"))
print(hashtags.split("#", 3)) # Split 3 and then stop

# Join
numbers = "1,2,3,4,5,6"
split_numbers = numbers.split(",")
print(split_numbers)
print(" → ".join(split_numbers))