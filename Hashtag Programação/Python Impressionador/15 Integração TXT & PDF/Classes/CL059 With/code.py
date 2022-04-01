"""
Using open, you can open a file .txt or .pdf
"""

file = open("test", "w")

file.write("Hello, my name's Matheus")

file.close()

with open("test2", "w") as file2: #file2 → Variable
    file2.write("Hello, my name's Matheus")
