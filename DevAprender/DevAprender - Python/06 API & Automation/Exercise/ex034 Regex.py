# 1 - Find the word "simples"
# ctrl + f = simples or \w{7}

# 2 - Find the occurrences of numbers 2 and 3 together
"""
dev123com
developer 123
dev = 123
dev = 1234
dev = 1337
dev 9000
"""
result = "23"

# 3 - Find the occurrences where the first number is 2 and whatever the next number
"""
dev123com
developer 123
dev = 124
dev = 1254
dev = 1337
dev 9000
"""

result = "2\d+"

# 4 - Using the values, find the full number
"""
13.35.86
22.36.77
53.12.34
"""

result = "\d\d\.\d\d\.\d\d"

# 5 - Jump where it says "pular"
"""
bah pular
tah encontrar
jah encontrar
nah encontrar
uai pular
"""

result = ["\w+ encontrar", "[tjn]\w+ encontrar", "[tjn]ah encontrar"]

# 6 - Jump where it says "pular"
"""
(123)1234-1235 encontrar
(123)1234-1235 encontrar
(129)1234-1235 pular
(129)1234-1235 pular
"""

result = ["[(]123[)]\d{4}[-]\d{4} encontrar", "[(]\d\d[3][)]\d{4}[-]\d{4}"]

# 7 - Jump where it says "pular"
"""
1234
6462 pular
"""

result = [1-4]

# 8 - Find only the letters starting between P and V
"""
pqrtsuv encontrar
wxyz pular
abcdefg pular
"""

result = "[p-v]"

# 9 - Create a regex to find "pizzas enviadas" ou "pizza enviada"
"""
2 pizzas enviadas
1 pizza enviada
3 pizzas enviadas
"""

result = "\d+ pizzas? enviadas?"