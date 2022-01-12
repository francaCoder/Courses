"""
Make a code that has a tuple with several words. And then, you must show the vowels for each word
"""

words = ("learn", "program", "language", "python", "course", "free", "study", "practice", "work", "mall", "developer", "feature", )
# Words = (str(input("Type a word: ")))

for word in words:
    print(f"\n In the word {word.upper()} we have → ", end="")
    for letter in word:
        if letter.lower() in "aeiou":
            print(letter, end=" ")



