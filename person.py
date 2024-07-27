from human import Human
class Person(Human):
    def __init__(self):
        Human.__init__()
    pass
    def poly(self):
        text3 = f"This is polyphormised method of class of Person. "
        print(text3)
        return text3
class Person1(Human):
    pass
    def poly(self):
        text4 = f"This is polyphormised method of class Person1."
        print(text4)
        return text4
person = Person("Nashali", 50, "Black", 5.3, 67)
person1 = Person1("Joel", 45, "white", 5.5, 75)
for pers in (person, person1):
    # print(person.name)
    # print(person)
    pers.poly()