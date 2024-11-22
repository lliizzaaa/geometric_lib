import unittest
from square import area, perimeter  # Импортируем функции из файла square.py


class TestSquareFunctions(unittest.TestCase):
    """Тесты для функций вычисления площади и периметра квадрата."""

    def test_area_positive(self):
        """Тест функции area для положительных значений стороны квадрата."""
        # Arrange
        side = 3
        expected_area = 9

        # Act
        result = area(side)

        # Assert
        self.assertEqual(result, expected_area)

    def test_area_zero(self):
        """Тест функции area для нулевого значения стороны."""
        # Arrange
        side = 0
        expected_area = 0

        # Act
        result = area(side)

        # Assert
        self.assertEqual(result, expected_area)

    def test_area_negative(self):
        """Тест функции area для отрицательных значений стороны."""
        # Arrange
        side = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_positive(self):
        """Тест функции perimeter для положительных значений стороны квадрата."""
        # Arrange
        side = 4
        expected_perimeter = 16

        # Act
        result = perimeter(side)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_zero(self):
        """Тест функции perimeter для нулевого значения стороны."""
        # Arrange
        side = 0
        expected_perimeter = 0

        # Act
        result = perimeter(side)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_negative(self):
        """Тест функции perimeter для отрицательных значений стороны."""
        # Arrange
        side = -4

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(side)


if __name__ == "__main__":
    unittest.main()
