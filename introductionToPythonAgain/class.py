class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self) -> tuple:
        return self.name, self.age

    def myfunc(self):
        print("Hello my name is " + self.name)


person1 = Person("Riccardo", 18)

print(person1())
person1.myfunc()
