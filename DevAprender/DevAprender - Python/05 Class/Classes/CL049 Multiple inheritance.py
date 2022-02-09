class Person:
    name = "I'm a person"

class Professional:
    name = "I'm a professional"

class Professional_actor(Person, Professional):
    pass


# print(Professional_actor.name) → "I'm a person" (Order)
# print(Professional_actor.mro()) → Mro show the order