class Person:
    #constructor
    def __init__(self,name,age,weight):
        #create instance variable
        self.name = name 
        self.age = age 
        self.weight = weight
    def walk(self):
        print(self.name ," can walk")
    def talk(self):
        print(self.name, " can talk")
    def eat(self):
        print(self.name, " can eat")
    def display(self):
        print(self.name, self.age, self.weight)
#create class type variable(object)
k1 = Person('kailash',21,51.25)
k1.walk()
k1.talk()
k1.eat()
k1.display()

name = input("Enter person name")
age = int(input("Enter age"))
weight = float(input("Enter weight"))

a1 = Person(name,age,weight)
a1.talk()
a1.walk()
a1.eat()
a1.display()
