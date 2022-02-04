#  ** = infinity nominal arguments (infinity Kwargs)

def concat(**words):
    phrase = ""
    for word in words.values():
        phrase += f"{word} "
    print(phrase)


concat(a="I'm", b="learning", c="Python")