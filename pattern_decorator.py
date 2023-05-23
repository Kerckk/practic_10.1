
class Coffee:
    def get_cost(self):
        pass

    def get_description(self):
        pass

class Espresso(Coffee):
    def get_cost(self):
        return 1.99

    def get_description(self):
        return "Espresso"

class CondimentDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()

class Milk(CondimentDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 0.59

    def get_description(self):
        return self._coffee.get_description() + ", Milk"

class Sugar(CondimentDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 0.39

    def get_description(self):
        return self._coffee.get_description() + ", Sugar"

coffee = Espresso()
print(coffee.get_description(), coffee.get_cost())

coffee = Milk(coffee)
print(coffee.get_description(), coffee.get_cost())

coffee = Sugar(coffee)
print(coffee.get_description(), coffee.get_cost())