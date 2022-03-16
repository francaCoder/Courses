revenues = 1000
print("The revenues was {}".format(revenues))
# .format() → Method, print() → Method

name = "matheus"
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.title())

email = "matheus@hotmail.com"
print(email.count("a"))
print(email.count("."))

# endswith
print(email.endswith("@hotmail.com")) # True

# startswith
print(email.startswith("matheus")) # True

# Find (returns the index)
print(email.find("@"))
print(email.index("@"))

# Types
print(email.isalpha()) # Letters or numbers
print(email.isalpha()) # Letters
print(email.isalnum()) # Numbers

# Replace
print(email.replace("@", "%"))

# Split
print(email.split("@"))

text = """ example1
example2
example3
"""
print(text.splitlines())

# Strip (Remove an empty spaces)