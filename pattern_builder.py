class Car:
    def __init__(self):
        self._wheels = None
        self._engine = None
        self._body = None

    def set_wheels(self, wheels):
        self._wheels = wheels

    def set_engine(self, engine):
        self._engine = engine

    def set_body(self, body):
        self._body = body

    def show_car_details(self):
        print(f"Number of wheels: {self._wheels}")
        print(f"Engine type: {self._engine}")
        print(f"Body type: {self._body}")

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_wheels(self, value):
        self.car.set_wheels(value)

    def set_engine(self, value):
        self.car.set_engine(value)

    def set_body(self, value):
        self.car.set_body(value)

    def get_car(self):
        return self.car

class Director:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_sports_car(self):
        self.builder.set_wheels(4)
        self.builder.set_engine("V6")
        self.builder.set_body("Coupe")

    def construct_city_car(self):
        self.builder.set_wheels(4)
        self.builder.set_engine("Electric")
        self.builder.set_body("Hatchback")

builder = CarBuilder()
director = Director(builder)

director.construct_sports_car()
car = builder.get_car()
car.show_car_details()

director.construct_city_car()
car = builder.get_car()
car.show_car_details()