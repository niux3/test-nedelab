from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    RED = 'rouge'
    BLUE = 'bleu'
    GREEN = 'vert'
    YELLOW = 'jaune'
    WHITE = 'blanc'
    BLACK = 'noire'


class Shape(Enum):
    ALU = "aluminium"
    STEEL = "acier"


class PaintType(Enum):
    ACRYLIC = "acrylique"
    METTALIC = "mettalique"


class Coating(Enum):
    LEATHER = 'cuir'
    NYLON = 'nylon'


class Item(ABC):
    __props = {}

    @abstractmethod
    def show_props(self, props):
        ...


class WheelRim(Item):
    def __init__(self, color, paint_type, shape):
        self.__props = {
            'color': color,
            'paint_type': paint_type,
            'shape': shape
        }

    def __str__(self):
        return "jante"

    def show_props(self):
        output = [
            f'couleur : {self.__props.get("color")}',
            f'type de peinture : {self.__props.get("paint_type")}',
            f'matière : {self.__props.get("paint_type")}',
        ]
        return "\n".join(output)
        

class Seat(Item):
    def __init__(self, color, coating):
        self.__props = {
            'color': color,
            'coating': coating,
        }

    def __str__(self):
        return "siège"

    def show_props(self):
        output = [
            f'couleur : {self.__props.get("color")}',
            f'matière : {self.__props.get("coating")}',
        ]
        return "\n".join(output)


class Car:
    __items = []

    def add_item(self, item):
        self.__items.append(item)

    def draw(self):
        for item in self.__items:
            print(item)
            print(item.show_props())


class CarBuilder:
    def prepare_luxury_car(self):
        car = Car()
        car.add_item(WheelRim(Color.BLACK.value, PaintType.METTALIC.value, Shape.ALU.value))
        car.add_item(Seat(Color.RED.value, Coating.LEATHER.value))
        return car

    def prepare_basic_car(self):
        car = Car()
        car.add_item(WheelRim(Color.YELLOW.value, PaintType.ACRYLIC.value, Shape.STEEL.value))
        car.add_item(Seat(Color.BLUE.value, Coating.NYLON.value))
        return car
        

        
def main():
    car = CarBuilder()
    car = car.prepare_luxury_car()
    print("Bentley")
    car.draw()
    print('*' * 80)
    car = CarBuilder()
    car = car.prepare_basic_car()
    print("Twingo")
    car.draw()
    

if __name__ == '__main__':
    main()
