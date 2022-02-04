"""
Create a function call generate_custom_object, that will receive 3 parameters, color, height, format. Your function should just show on screen what was passed to it.

- The first parameter should be positional
- The format and height parameters must be necessarily nominal.
"""


def generate_custom_object(color, *, height, format):
    print(f"\nColor → {color} \nHeight → {height:.2f} \nFormat → {format}")


generate_custom_object("Blue", height=2.10, format="Square")