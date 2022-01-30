"""
Make a program that has a function called write(), that will receive any text with parameter and show a custom lines.
ex:
write(hello)

output:
---------
  hello
---------

write(exemple)

output:
-------------
   exemple
-------------
"""


def write(msg):
    print("---", end="")
    print("-" * len(msg))
    print(f"{msg:<3}")
    print("---", end="")
    print("-" * len(msg))


write("Hello")