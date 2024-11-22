import unittest
from triangle import area, perimeter

class TestTriangleCalculations(unittest.TestCase):

    def test_area_positive(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0, places=5)  #Прямоугольный треугольник
        self.assertAlmostEqual(area(7, 8, 10), 27.810744326608734, places=4) #Пример тупоугольного треугольника
        self.assertAlmostEqual(area(6, 8, 10), 24.0, places=5)  #Пример остроугольного треугольника


    def test_area_zero(self):
        with self.assertRaises(ValueError): # Вырожденный треугольник не существует
            area(0,0,0)


    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(7, 8, 10), 25)


    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0) #Вырожденный треугольник, периметр 0


    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1,2,5) #1+2<5 - Треугольник не существует



if __name__ == '__main__':
    unittest.main()

