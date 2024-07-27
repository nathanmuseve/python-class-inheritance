from human import Human # Class Inheritance form Human class, Imported Human class from human module

class Nathan(Human): #class inherintance
    def __init__(self, name, age, color, height, weight, state, marital):
        super().__init__(name, age, color, height, weight, state) #class Nathan inherits all properties and methods from class Human.But it also has its own methods
        self.marital = marital
    def walk(self): #common function in all classes
        text3 = f"{self.name} I rarely cry!"
        print(text3)
        return text3
class James(Nathan): #class james inherits all properties and methods from Class Nathan that also inherits some of the class Human props and methods
    pass
    def walk(self): # a common function in all classes
        text4 = f"{self.name} laughs always."
        print(text4)
        return text4
human = Human("PARENT CLASS", 95, "COLOUR", 6, 89, "MARRIED")
nathan = Nathan("Nathan", 95, "COLOUR", 6, 89, "not yet", "Yes")
james = James("Joel", 24, "white", 4.5, 60, "Not married", "No")
for pers in (human, nathan,james):
    pers.walk()
human.description()
nathan.career()
