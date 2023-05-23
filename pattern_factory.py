from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory:
    def __init__(self):
        self._animals = dict()

    def register_animal(self, name, animal):
        self._animals[name] = animal()

    def create_animal(self, name):
        animal = self._animals.get(name)
        if not animal:
            raise ValueError("Invalid animal name")
        return animal

animal_factory = AnimalFactory()
animal_factory.register_animal("dog", Dog)
animal_factory.register_animal("cat", Cat)

animal = animal_factory.create_animal("dog")
print(animal.speak())

animal = animal_factory.create_animal("cat")
print(animal.speak())
