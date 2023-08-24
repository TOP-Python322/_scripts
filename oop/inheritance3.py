class Vehicle:
    wheels: int = 4

    def __init__(self, average_speed: int):
        self.speed = average_speed

    def move(self):
        print(f'{self.__class__.__name__} moves with average speed of {self.speed} km/h')


class Bicycle(Vehicle):
    wheels: int = 2


class Car(Vehicle):
    pass


class Train(Vehicle):
    wheels: int = 16

    def move(self):
        print(f'{self.__class__.__name__} moves along railroads with average speed of {self.speed} km/h')


# пример скорее неудачного наследования, так как в данном классе переопределены все атрибуты базового класса, следовательно с базовым классом его де-факто ничего не связывает
class Aircraft(Vehicle):
    wheels: int = 3

    def __init__(self, average_ground_speed: int, average_fly_speed: int):
        # Vehicle.__init__(self, average_ground_speed)
        super().__init__(average_ground_speed)
        self.fly_speed = average_fly_speed

    def move(self):
        print(f'{self.__class__.__name__} moves on the ground with average speed of {self.speed} km/h')

    def fly(self):
        print(f'{self.__class__.__name__} moves in the air with average speed of {self.fly_speed} km/h')


# >>> vehicle = Vehicle(30)
# >>>
# >>> vehicle.wheels
# 4
# >>> vehicle.move()
# Vehicle moves with average speed of 30 km/h

# >>> haro = Bicycle(18)
# >>>
# >>> haro.wheels
# 2
# >>> haro.move()
# Bicycle moves with average speed of 18 km/h

# >>> volga = Car(70)
# >>>
# >>> volga.wheels
# 4
# >>> volga.move()
# Car moves with average speed of 70 km/h

# >>> sapsan = Train(130)
# >>>
# >>> sapsan.wheels
# 16
# >>> sapsan.move()
# Train moves along railroads with average speed of 130 km/h

# >>> an2 = Aircraft(50, 500)
# >>>
# >>> an2.wheels
# 3
# >>> an2.move()
# Aircraft moves on the ground with average speed of 50 km/h
# >>>
# >>> an2.fly()
# Aircraft moves in the air with average speed of 500 km/h

