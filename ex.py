#!/usr/bin/envpython3
class Person:
    def __init__(self, n,a):
        self.name=n
        self.age=a
    def describe(self):
        print("Name:", self.name)
        print("Age:", self.age)
    def __lt__(self, other):
        return self.age <other.age
    def __str__(self):
        return f"My name is {self.name}. I am {self.age}."

macron = Person("Emmanuel Macron", 43)
macron.describe()
print(macron)
biden = Person("JoeBiden",78)
print(f"Macron isyounger: {macron <biden}")

class Employee:
    def work(self):
        print("I should be paid...")
class President(Person,Employee):
    def set_term(self,term):
        print(f"Setting term to {term}")
        self.term=term

print("MacronisnowPresident")
macron = President("EmmanuelMacron",43)
macron.set_term(25) #from President
macron.describe() #from Person

print(f"Macron is President:{isinstance(macron, President)}")
print(f"Macron is Person:{isinstance(macron, Person)}")
print(f"President is Person:{issubclass(President, Person)}")
print(f"Person is President:{issubclass(Person, President)}")



print("Macron is now President")
macron = President("Emmanuel Macron", 43)
macron.set_term(25)
macron.describe()
macron.work()
