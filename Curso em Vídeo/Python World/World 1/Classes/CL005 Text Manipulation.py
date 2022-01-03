phrase = "Curso em Video Python"

# In backstage, each letter is an element
# Index:  C = 0   u = 1   r = 2   s = 3   o = 4   .....

# "Slice"
# If i want show a letter:

print(phrase)
print(phrase[9])

# If i want show a part:
print(phrase[9:14])
# He deletes the last

# Show a part jumping 2 by 2
print(phrase[9:21:2])

# When i don't put the first number, he starts from the beginning and go to the end
print(phrase[:21])

# When i don't put the second number, he starts from number and go to the end
print(phrase[:0])

# Starts from 9, go to the end jumping 3 by 3
print(phrase[9::3])


# analyze

# Length
len(phrase)

# Count
# How much letters ' o ' exist inside string
phrase.count("o")

# How much ' o ' among 0 - 13
phrase.count("o", 0, 13)

# He will return where does the sentence start or -1 case he don't find
phrase.find("deo")

# Or  'element' in 'object'

# Boolean
print("Curso" in phrase)


# Transformation
# Replace

# It will look for python and will do the replace
print(phrase.replace("Python", "Android"))


# Upper - Capital
print(phrase.upper())

# Lower - Tiny
print(phrase.lower())

# Capitalize - Only the first letter will be in upper
print(phrase.capitalize())

# Title - How many words have your string and do the capitalize word by word
print(phrase.title())

newPhrase = "   Aprenda Python  "

# In the world of technology, we need to think in users.
# Oftentimes the peoples do unnecessary things, for exemple: spaces
# 3 Spaces before and 2 spaces after

# Strip - Remove the unnecessary spaces
print(newPhrase.strip())

# rstrip - Right  lstrip - Left


# Division

# Split - Per pattern, the division is made in empty spaces and after this, each word
# becomes an element within an array
phrasesplit = phrase.split()
print(phrasesplit)

# Join - Join the elements of array using - between them
print("-".join(phrasesplit))
