"""
Make a code that read the phrase and show:
- How many times does the letter ' a ' appear
- In which position appeared the first time
- In which position appeared the last time




phrase = "Que repousa sobre um acontecimento incerto, fortuito. Diz-se de uma grandeza"

print("The letter ' a ' appeared {} times".format(phrase.count("a")))
print("The letter ' a ' appeared for the first time in {} index.".format(phrase.find("a")))
print("The letter ' a ' appeared for the last time in {} index.".format(phrase.rfind("a")))
"""

phrase = str(input("Type a Phrase: ")).strip().upper()

print("The letter ' a ' appeared {} times in phrase.".format(phrase.count("A")))
print("The letter ' a ' appeared for the first time in {} index.".format(phrase.find("A") + 1))
print("The letter ' a ' appeared for the last time in {} index.".format(phrase.rfind("A") + 1))



