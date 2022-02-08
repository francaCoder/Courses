from operator import itemgetter

people = [
    {
        "Name": "Matheus",
        "Age": 18,
        "Access_level": 3
    },
    {
        "Name": "Carlos",
        "Age": 24,
        "Access_level": 1
    },
    {
        "Name": "Bruna",
        "Age": 15,
        "Access_level": 4
    },
    {
        "Name": "Carol",
        "Age": 44,
        "Access_level": 2
    }
]

people.sort(key=itemgetter('Access_level'))
print(people)


# Tuple

products = [
    ("Cell", 1000),
    ("Bicycle", 500),
    ("TV", 2000),
]

products.sort(key=itemgetter(1))
# or
# products.sort(key=itemgetter(1), reverse=True)

print(products)