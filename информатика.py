from typing import Iterable


class Rectengl:
    def __init__(self, area: float, perimeters: float,side1,side2) -> None:
        self._area =...
        self._perimeters =...
        side1=3
        side2=6


    def get_1(self) -> float:
        self._area=side1 * side2
        return self._area

    def get_2(self) -> float:
        self._perimeters=side1 + side2
        return self._perimeters



class Square(Rectengl):
    def __init__(self, area: float, perimeters: float,side1,side2) -> None:
        self._area = ...
        self._perimeters = ...

    def get_3(self) -> float:
        self._area=side1 * side2
        return self._area

    def get_4(self) -> float:
        self._perimeters=side1 + side2
        return self._perimeters


print()