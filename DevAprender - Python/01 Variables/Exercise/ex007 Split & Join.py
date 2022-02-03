"""
1 - Transform the phrase1 in a list of words and save the result in a variable called words1
2 - Transform the phrase2 in a list of words and save the result in a variable called words2
3 - Change the words1's content to: "Challenge,string's,manipulation"
4 - Change the words2's content to: "Matheus & Maria & João & David"
"""

phrase1 = "Challenge string's manipulation"
words1 = phrase1.split()
print(",".join(words1))

phrase2 = "Matheus,Maria,João,David"
words2 = phrase2.split(",")
print(" & ".join(words2))