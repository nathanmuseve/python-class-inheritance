# Class creation
class Human: # Main class
    def __init__(self, name, age, color, height, weight, state): #class attributes/properties
        self.name = name
        self.age = age
        self.color = color
        self.height = height
        self.weight = weight
        self.state = state
        
    def walk(self): #this will be poly function
        message = f"{self.name} do walk daily!"
        print(message)
        return message
    
    def description(self): #class instance/ behaviour(method)
        text = f"My name is {self.name}. I am {self.age} years old. My siblings love {self.color} clothes.Our father is the tallest man in the house by {self.height}feet. His weight is far much heavier than all of us. He weighs {self.weight}kgs."
        print(text)
        return text
    
    def status(self): #class instance/ behaviour(method)
        text1 = f"I am {self.state} for about {self.age} years old now."
        print(text1)
        return text1
    
    def career(self): #method
        text4 = f"Worked for {self.age} years."
        print(text4)
        return text4
    
desc = Human("PARENT CLASS", 95, "COLOUR", 6, 89, "MARRIED")
stat = Human("PARENT CLASS", 65, "COLOUR", 6, 89, "MARRIED")
car = Human("PARENT CLASS", 55, "COLOUR", 6, 89, "MARRIED")

desc.description() #method call form Human class
stat.status() # method call from Human class
car.career() #inherited  method from Human class


    
        
            