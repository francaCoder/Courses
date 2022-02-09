# Magicdunder (Magic methods, dunder methods, double underscore)

class Person:
    def __init__(self):
        self.name = "I'm a person"
        self.skills = ["Skill1", "Skill2", "Skill3"]

    def __repr__(self):
        return f"Class Person with name and skills"

    def __len__(self):
        #len(Person)
        return len(self.skills)

    def __str__(self):
        return f"{self.name} with skills {self.skills}"




person = Person()
print(person.name)
print(repr(person))
print(len(person)) # Len(skills)
print(person) # Str
print(dir(person))