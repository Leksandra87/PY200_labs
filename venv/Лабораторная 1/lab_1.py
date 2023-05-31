import doctest


class Box:
    def __init__(self, volume: float, used_volume: float, color: str, material: str):
        """
        Создание и подготовка к работе обьекта "Коробка"
        :param volume: объем коробки
        :param used_volume: заполненный обьем коробки
        :param color: цвет коробки
        :param material: материал, из которого состоит коробка

        Примеры:
        >>> box_1 = Box(200, 0, 'green', 'wood')  # инициализация экземпляра класса
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем коробки должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем коробки должен быть положительным числом")
        self.volume = volume
        if not isinstance(used_volume, (int, float)):
            raise TypeError("Используемый объем коробки должен быть int или float")
        if used_volume < 0:
            raise ValueError("Используемый объем не может быть отрицательным числом")
        self.used_volume = used_volume
        if not isinstance(color, str):
            raise TypeError("Название цвета должно быть типа str")
        self.color = color
        if not isinstance(material, str):
            raise TypeError("Название материала должно быть типа str")
        self.material = material

    def is_empty_box(self) -> bool:
        """
        Функция которая проверяет является ли коробка пустой

        :return: Является ли стакан пустым

        Примеры:
         >>> box = Box(200, 0, 'green', 'wood')
         >>> box.is_empty_box()
        """
        if self.used_volume == 0:
            return True
        else:
            return False

    def add_something_to_box(self, something: float) -> None:
        """
        Добавление содержимого в коробку.
        :param something: Объем добавляемого чего-то

        :raise ValueError: Если количество добавляемого содержимого превышает свободное место в коробке,
        то вызываем ошибку

        Примеры:
         >>> box = Box(200, 0, 'green', 'wood')
         >>> box.add_something_to_box(200)
        """
        if not isinstance(something, (int, float)):
            raise TypeError("Добавляемое содержимое должно быть типа int или float")
        if something < 0:
            raise ValueError("Добавляемое содержимое должно быть положительным числом")
        if something > (self.volume - self.used_volume):
            raise ValueError("Недостаточно места в коробке")
        self.used_volume += something

    def remove_something_from_box(self, something: float) -> None:
        """
        Извлечение чего-то из коробки.

        :param something: Объем извлекаемого вещества
        :raise ValueError: Если количество извлекаемого  превышает объем содержимого,
        то возвращается ошибка.

        Примеры:
         >>> box = Box(500, 500,'green', 'wood')
         >>> box.remove_something_from_box(200)
        """
        if not isinstance(something, (int, float)):
            raise TypeError("Извлекаемое содержимое должно быть типа int или float")
        if something < 0:
            raise ValueError("Извлекаемое содержимое должно быть положительным числом")
        if something > self.used_volume:
            self.used_volume = 0
        else:
            self.used_volume -= something
        ...

    def repaint_box(self, new_color: str) -> None:
        """
        Перекрасить коробку.

        :param new_color: Цвет, в который будет перекрашена коробка

        Примеры:
         >>> box = Box(500, 500,'green', 'wood')
         >>> box.repaint_box("зеленый")
        """
        if not isinstance(new_color, str):
            raise TypeError("Название цвето должно быть типа str")
        self.color = new_color
        ...

    def __str__(self) -> str:
        """
        Возвращает строку с читаемой информацией об объекте

        Пример:
        >>> box = Box(500, 500,'зеленый', 'керамика')
        >>> box.__str__()
        """
        return f"Коробка объмом {self.volume}, заполнена на {self.used_volume},{self.color} цвета из {self.material}"


class Pencil:
    def __init__(self, line_thickness: float, color: str):
        """
        Создание объекта "Карандаш"
        :param color: цвет карандаша
        :param line_thickness: толщина линии

        Пример:
        >>> pen = Pencil(0.5, 'сиреневый')
        """
        if not isinstance(line_thickness, (int, float)):
            raise TypeError('Толщина линии должна быть типа int или float')
        if not 0 < line_thickness <= 2:
            raise ValueError('Толщина линии должна быть положительной, но не может превышать 2 мм')
        self.line_thickness = line_thickness
        if not isinstance(color, str):
            raise TypeError('Название цвета карандаша должно быть типа str')
        self.color = color

    def print_line(self, len_: float):
        """
        Карандаш рисует линию
        :param len_: длина линии

        Пример:
        >>> pen = Pencil(0.5, 'сиреневый')
        >>> pen.print_line(100)
        """
        if not isinstance(len_, (int, float)):
            raise TypeError('Длина линии должна быть типа int или float')
        if self.line_thickness >= 2:
            raise ValueError('Тупым карандашом рисовать нельзя, поточите')
        print(f'Нарисована линия {len_}см {self.color} цвета')
        eras = 0.02  # карандаш притупляется при письме на величину eras за каждый см линии
        if len_ * eras >= 2 - self.line_thickness:
            print('Карандаш затупился, требуется поточить')
            self.line_thickness = 2
        else:
            self.line_thickness += len_ * eras

    def sharp_pencil(self):
        """
        Точим карандаш

        Пример:
        >>> pen = Pencil(1.9, 'сиреневый')
        >>> pen.sharp_pencil()
        """
        self.line_thickness = 0.5
        print('Карандаш поточили, можете рисовать дальше')

    def __str__(self) -> str:
        """
        Возвращает строку с читаемой информацией об объекте
        """
        return f'Карандаш ({self.color}) цвета с диаметром стержня ({self.line_thickness})мм'


if __name__ == "__main__":
    doctest.testmod()
