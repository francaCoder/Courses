"""
Make a code that show on screen a countdown to the explosion of fireworks starts from 10 and going
to 0, with a 1 second pause between these
"""

from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print("Happy new year!!!!!")