"""
Find out the index of letter "a" inside variable called library
"""

library = "Library"
print(library[4])
print(library.find("a"))
print(library.find("ary")) # Starts from index 4
print(library.rindex("a"))
print(library.index("a"))

# Using the phrase: "Using python applications."
# print just "python applications."
phrase = "Using python applications."
# print(phrase[6:].title())
index_p = phrase.index("p")
print(phrase[index_p:].title())