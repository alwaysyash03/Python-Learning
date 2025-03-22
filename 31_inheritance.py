# Inheritance is a mechanism in which one class can inherit the properties and methods of another class.
# Inheritance is a mechanism for reusing code
class Mammal: # Parent class
    def walk(self):
        print("Walk")


class Dog(Mammal): # Child class
    def bark(self):
        print("Bark")
    
class Cat(Mammal):
  pass# Pass is used to define a class with no methods or attributes

dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.walk()
