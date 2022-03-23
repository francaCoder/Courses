# New functions

import webbrowser as web

# web.open("https://hashtagtreinamentos.com")


import time

# Time()
print(time.time())
print(time.ctime())

initial_time = time.time()
for c in range(100000000):
    pass
final_time = time.time()
print(f"The program took {final_time - initial_time} seconds to run")

# Sleep
#...


print(time.gmtime())