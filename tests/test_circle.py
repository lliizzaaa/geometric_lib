import unittest
import math
from circle import area, perimeter  # Импортируем функции из модуля circle


class TestCircleFunctions(unittest.TestCase):
    """Тесты для функций вычисления площади и периметра круга."""

    def test_area_positive(self):
        """Тест функции area для положительных значений радиуса."""
        # Arrange
        radius = 3
        expected_area = math.pi * radius**2

        # Act
        result = area(radius)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=5)

    def test_area_zero(self):
        """Тест функции area для радиуса равного нулю."""
        # Arrange
        radius = 0
        expected_area = 0

        # Act
        result = area(radius)

        # Assert
        self.assertEqual(result, expected_area)

    def test_area_negative(self):
        """Тест функции area для отрицательных значений радиуса."""
        # Arrange
        radius = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            area(radius)

    def test_perimeter_positive(self):
        """Тест функции perimeter для положительных значений радиуса."""
        # Arrange
        radius = 5
        expected_perimeter = 2 * math.pi * radius

        # Act
        result = perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, expected_perimeter, places=5)

    def test_perimeter_zero(self):
        """Тест функции perimeter для радиуса равного нулю."""
        # Arrange
        radius = 0
        expected_perimeter = 0

        # Act
        result = perimeter(radius)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_negative(self):
        """Тест функции perimeter для отрицательных значений радиуса."""
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(radius)


if __name__ == "__main__":
    unittest.main()
