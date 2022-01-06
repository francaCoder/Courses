# Read a phrase and answer if it is a palindrome, disregarding the spaces

phrase = str(input("Type a phrase: ")).strip().upper()
words = phrase.split()
join = ''.join(words)
reverse = join[::-1]

"""
for letter in range(len(join) - 1, -1, -1):
    reverse += join[letter]
"""


print("The inverse of {} is {}".format(join, reverse))
if reverse == join:
    print("He have a palindrome.")
else:
    print("The typed phrase isn't a palindrome.")