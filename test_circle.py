import unittest
import math
from shapes.circle import area, perimeter


class TestCircleArea(unittest.TestCase):
    """Тесты для функции area."""

    def test_area_positive(self):
        """Проверяет площадь для положительных значений радиуса (Arrange-Act-Assert)."""
        r = 3  # Arrange
        expected = math.pi * r * r  # Arrange
        result = area(r)  # Act
        self.assertAlmostEqual(result, expected, places=5)  # Assert

    def test_area_zero(self):
        """Проверяет площадь для радиуса, равного 0."""
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        """Проверяет, что функция вызывает исключение при отрицательном радиусе."""
        with self.assertRaises(ValueError):
            area(-3)


class TestCirclePerimeter(unittest.TestCase):
    """Тесты для функции perimeter."""

    def test_perimeter_positive(self):
        """Проверяет периметр для положительных значений радиуса."""
        r = 3  # Arrange
        expected = 2 * math.pi * r  # Arrange
        result = perimeter(r)  # Act
        self.assertAlmostEqual(result, expected, places=5)  # Assert

    def test_perimeter_zero(self):
        """Проверяет периметр для радиуса, равного 0."""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        """Проверяет, что функция вызывает исключение при отрицательном радиусе."""
        with self.assertRaises(ValueError):
            perimeter(-3)


if __name__ == "__main__":
    unittest.main()
