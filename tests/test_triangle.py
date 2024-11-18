import unittest
from triangle import area, perimeter  # Импортируем функции из модуля triangle


class TestTriangleFunctions(unittest.TestCase):
    """Тесты для функций вычисления площади и периметра треугольника."""

    def test_area_positive(self):
        """Тест функции area для корректного треугольника с положительными сторонами."""
        # Arrange
        a, b, c = 3, 4, 5
        expected_area = 6.0

        # Act
        result = area(a, b, c)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=5)

    def test_area_invalid_triangle(self):
        """Тест функции area для некорректного треугольника."""
        # Arrange
        a, b, c = 1, 2, 5  # Не выполняется неравенство треугольника

        # Act & Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_area_zero(self):
        """Тест функции area для треугольника со сторонами, равными нулю."""
        # Arrange
        a, b, c = 0, 0, 0

        # Act & Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_area_negative(self):
        """Тест функции area для треугольника с отрицательной стороной."""
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_perimeter_positive(self):
        """Тест функции perimeter для корректного треугольника с положительными сторонами."""
        # Arrange
        a, b, c = 3, 4, 5
        expected_perimeter = 12

        # Act
        result = perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_invalid_triangle(self):
        """Тест функции perimeter для некорректного треугольника."""
        # Arrange
        a, b, c = 1, 2, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_perimeter_zero(self):
        """Тест функции perimeter для треугольника со сторонами, равными нулю."""
        # Arrange
        a, b, c = 0, 0, 0

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_perimeter_negative(self):
        """Тест функции perimeter для треугольника с отрицательной стороной."""
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(a, b, c)


if __name__ == "__main__":
    unittest.main()
