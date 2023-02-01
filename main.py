  #  Задание 1

import time
import enum


class Colour(enum.Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2


class TrafficLight:
    __colour: Colour
    __move: int = 1

    def __init__(self, colour: Colour) -> None:
        self.__colour = colour

    def running(self, green_t=7, red_t=7, yellow_t=2):

        for _ in range(10):  
            if self.__colour == Colour.RED:
                print(self.__colour.name)
                time.sleep(red_t)
            elif self.__colour == Colour.YELLOW:
                print(self.__colour.name)
                time.sleep(yellow_t)
            elif self.__colour == Colour.GREEN:
                print(self.__colour.name)
                time.sleep(green_t)

            if self.__colour.value == 2:
                self.__move = -1
            elif self.__colour.value == 0:
                self.__move = 1

            self.__colour = Colour(self.__colour.value + self.__move)


if __name__ == "__main__":
    traffic = TrafficLight(Colour.GREEN)
    traffic.running()

#  Задание 2

class Road:

    _length: float
    _width: float

    def __init__(self, length: float = 0, width: float = 0) -> None:
        self._length = length
        self._width = width

    def calc(self, density: float, thickness: float) -> float:
        return self._length * self._width * density * thickness


if __name__ == "__main__":
    road = Road(length=20, width=5000)
    print(road.calc(25, 5))

    # or if we in module
    road = Road()
    road._length = 20
    road._width = 5000
    print(road.calc(density=25, thickness=5))

#  Задание 3
class Worker:
    name: str
    surname: str
    position: str
    _income: dict = {"wage": 0.0, "bonus": 1.0}

    def __init__(self, name: str, surname: str, position: str, income: dict = {"wage": 0, "bonus": 1.0}) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


#  Задание 4

from enum import Enum


class TURN(Enum):
    LEFT = 0
    RIGHT = 1


class Car:
    speed: float
    _colour: str  
    _name: str
    _is_police: bool = False

    def __init__(self, colour, name) -> None:
        self._colour = colour
        self._name = name

    def go(self) -> None:
        print(f"{self._name} is start")

    def stop(self) -> None:
        print(f"{self._name} is stop")

    def turn(self, turn_side: TURN) -> None:
        print(f"{self._name} is turn to {turn_side.name}")

    def show_speed(self) -> float:
        return self.speed


class TownCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)

    def show_speed(self) -> float:

        spd = super().show_speed()

        if spd > 40:
            print("Overspeed (40)")

        return spd


class SportCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)


class WorkCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)

    def show_speed(self) -> float:
        spd = super().show_speed()

        if spd > 60:
            print("Overspeed (60)")

        return spd


class PoliceCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)
        self._is_police = True


if __name__ == "__main__":
    abstract_car = Car("Transparent", "SomeCar")
    town_car = TownCar("Black", "TownCar")
    work_car = WorkCar("Green", "WorkCar")
    police_car = PoliceCar("DarkBlue", "PoliceCar")

    abstract_car.speed = -100 # =)
    town_car.speed = 120
    work_car.speed = 160
    police_car.speed = 175

    for some in [abstract_car, town_car, work_car, police_car]:
        print(f"{some.__class__}._name = {some._name}")
        print(f"{some.__class__}._colour = {some._colour}")
        print(f"{some.__class__}._is_police = {some._is_police}")

        print(f"{some.__class__}.go() => ", end="")
        some.go()

        print(f"{some.__class__}.stop() => ", end="")
        some.stop()

        print(f"{some.__class__}.turn(TURN.RIGHT) => ", end="")
        some.turn(TURN.RIGHT)

        print(f"{some.__class__}.turn(TURN.LEFT) => ", end="")
        some.turn(TURN.LEFT)

        print(f"{some.__class__}.show_speed() => {some.show_speed()}", end="\n\n")

  #  Задание 5
class Stationery:
    title: str

    def draw(self) -> None:
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "ручка"

    def draw(self) -> None:
        print("Пишем текст")
        return None


class Pencil(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "карандаш"

    def draw(self) -> None:
        print("Чертим чертеж")
        return None


class Handle(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "маркер"

    def draw(self) -> None:
        print("Выделяем заголовки")
        return None


if __name__ == "__main__":
    pen = Pen()
    pencil = Pencil()
    handle = Handle()

    for some in [pen, pencil, handle]:
        print(f"{some.__class__}:title = {some.title}")
        print(f"{some.__class__}.draw() =>\t", end="")
        some.draw()
        print()