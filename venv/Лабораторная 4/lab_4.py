from math import pi
from typing import Union


class FlatForm:
    """
     Класс некая плоская фигура, имеет два параметра:
     color: цвет фигуры, может быть изменен
     area: площадь фигуры в сантиметрах, устанавливается только при инициализации
     """

    def __init__(self, color: str, area: Union[int, float]) -> None:
        self._area = None
        self.init_area(area)
        self.color = color

    @staticmethod
    def is_valid(value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError
        if value <= 0:
            raise ValueError

    def init_area(self, area: Union[int, float]) -> None:
        self.is_valid(area)
        self._area = area

    @property
    def area(self) -> Union[int, float]:
        return self._area

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError
        self._color = color

    def value_in_meters(self) -> float:
        """ Возвращает значение площади в метрах """
        meters = 10000
        area_in_meters = self._area / meters
        return area_in_meters

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(color={self._color}, area={self._area})"

    def __str__(self) -> str:
        return f"Фигура {self._color} цвета площадью {self._area}см2"

    @classmethod
    def what_is_it(cls):
        print(f'Это объект класса {cls.__name__}')


class Circle(FlatForm):
    """ Класс круг, дочерний класс от плоской фигуры"""

    def __init__(self, color: str, area: Union[int, float]) -> None:
        super().__init__(color, area)
        self._radius = None
        self.init_radius()

    def init_radius(self):
        """ Метод вычисляет радиус по площади и устанавливает атрибут радиус. """
        radius = round((self.area / pi) ** 0.5, 4)
        self._radius = radius

    def perimeter(self):
        """ Метод вычисляет длину окружности """
        perimeter = round(2 * self._radius * pi, 4)
        return perimeter

    @property
    def radius(self) -> Union[int, float]:
        return self._radius

    def __str__(self) -> str:
        return f"Круг {self._color} цвета площадью {self._area}см2"


class Rectangle(FlatForm):
    """
    Класс прямоугольник, дочерний от плоской фигуры,
    помимо цвета и площади принимает еще один аргумент
    - длину одной из сторон (в сантиметрах)
    """

    def __init__(self, color: str, area: Union[int, float], width: Union[int, float]) -> None:
        super().__init__(color, area)
        self.width = width
        self._length = None
        self.init_length()

    @property
    def width(self) -> Union[int, float]:
        return self._width

    @width.setter
    def width(self, width: Union[int, float]) -> None:
        self.is_valid(width)
        self._width = width
        self.init_length()

    def init_length(self) -> None:
        """ Метод вычисляет вторую сторону прямоугольника по первой стороне и площади и устанавливает атрибут"""
        self._length = round(self.area / self.width, 4)

    @property
    def length(self) -> Union[int, float]:
        return self._length

    def perimeter(self) -> Union[int, float]:
        """ Метод вычисляет периметр прямоугольника """
        perimeter = 2 * self._length + 2 * self._width
        return perimeter

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(color={self._color}, area={self._area}, width={self._width})"

    def __str__(self) -> str:
        return f"Прямоугольник {self._color} цвета площадью {self._area}см2, ({self._length})X({self._width})"


class Ball(Circle):
    """
    Класс шар, дочерний от класса круг. Принимает при инициализации два аргумента:
    color: цвет
    area: площадь сечения
    """

    def get_volume(self) -> float:
        """ Метод определяет объем шара в сантиметрах """
        volume = round(4 / 3 * pi * self.radius ** 3, 4)
        return volume

    def volume_in_meters(self) -> float:
        """ Метод определяет объем шара в метрах """
        meters = 1000000
        volume = self.get_volume() / meters
        return volume

    def surface_area(self) -> float:
        """ Метод определяет площадь поверхности шара в сантиметрах """
        area = 4 * pi * self.radius ** 2
        return area

    def __str__(self) -> str:
        return f"Шар {self._color} цвета объемом {self.get_volume()}см3 и радиусом {self.radius} см"

    ...


if __name__ == "__main__":
    c = Ball('green', 1000)
    print(c)
    c.what_is_it()
