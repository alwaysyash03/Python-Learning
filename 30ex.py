class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f'Hi , I am {self.name}.')

Yash = Person("Yash Kumar")
print(Yash.name)
Yash.talk()  # Output: Talk

Ishita = Person("Ishita Thakar")
Ishita.talk()