import unittest
from lab_4 import Rectangle  # импортируем то, что будем тестировать

COLOR = 'red'
AREA = 200
WIDTH = 10


class TestRectangle(unittest.TestCase):

    def setUp(self):
        """ Устанавливаем данные для тестирования """

        self.my_rec = Rectangle(COLOR, AREA, WIDTH)

    def test_init(self):
        """ Проверяет корректность формирования атрибутов при инициализации"""
        self.assertEqual(self.my_rec.color, COLOR)
        self.assertEqual(self.my_rec.area, AREA)
        self.assertEqual(self.my_rec.width, WIDTH)
        self.assertEqual(self.my_rec.length, round(AREA / WIDTH, 4))

    def test_perimeter(self):
        """ Проверяет метод рассчета периметра"""
        self.assertEqual(self.my_rec.perimeter(), 2 * WIDTH + 2 * self.my_rec.length)

    def test_is_valid(self):
        """ Тест метода проверяющего корректность вводимых данных"""
        with self.assertRaises(TypeError):
            self.my_rec.color = 2
            self.my_rec.init_area([1])
            self.my_rec.width = 'frfr'
        with self.assertRaises(ValueError):
            self.my_rec.width = 0
            self.my_rec.init_area(-30)

    def test_str(self):
        """ Проверяет вывод данных """
        self.assertEqual(self.my_rec.__str__(),
                         f"Прямоугольник {COLOR} цвета площадью {AREA}см2, "
                         f"({self.my_rec.length})X({WIDTH})")
        ...


if __name__ == '__main__':
    unittest.main()
