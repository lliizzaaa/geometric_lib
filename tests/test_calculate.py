import unittest
from calculate import calc  # Импортируем изменённую функцию calc

class TestCalc(unittest.TestCase):
    """Тесты для функции calc."""

    def test_calc_circle_area(self):
        """Тест calc для корректного вычисления площади круга."""
        # Arrange
        figure = 'circle'
        function = 'area'
        size = [3]
        expected_message = 'area of circle is 28.274333882308138'
        expected_result = 28.274333882308138

        # Act
        message, result = calc(figure, function, size)

        # Assert
        self.assertEqual(message, expected_message)
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_calc_circle_perimeter(self):
        """Тест calc для корректного вычисления периметра круга."""
        # Arrange
        figure = 'circle'
        function = 'perimeter'
        size = [3]
        expected_message = 'perimeter of circle is 18.84955592153876'
        expected_result = 18.84955592153876

        # Act
        message, result = calc(figure, function, size)

        # Assert
        self.assertEqual(message, expected_message)
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_calc_square_area(self):
        """Тест calc для корректного вычисления площади квадрата."""
        # Arrange
        figure = 'square'
        function = 'area'
        size = [4]
        expected_message = 'area of square is 16'
        expected_result = 16

        # Act
        message, result = calc(figure, function, size)

        # Assert
        self.assertEqual(message, expected_message)
        self.assertEqual(result, expected_result)

    def test_calc_square_perimeter(self):
        """Тест calc для корректного вычисления периметра квадрата."""
        # Arrange
        figure = 'square'
        function = 'perimeter'
        size = [4]
        expected_message = 'perimeter of square is 16'
        expected_result = 16

        # Act
        message, result = calc(figure, function, size)

        # Assert
        self.assertEqual(message, expected_message)
        self.assertEqual(result, expected_result)

    def test_invalid_figure(self):
        """Тест calc для неподдерживаемой фигуры."""
        # Arrange
        figure = 'triangle'
        function = 'area'
        size = [3]

        # Act & Assert
        with self.assertRaises(AssertionError):
            calc(figure, function, size)

    def test_invalid_function(self):
        """Тест calc для неподдерживаемой функции."""
        # Arrange
        figure = 'circle'
        function = 'volume'
        size = [3]

        # Act & Assert
        with self.assertRaises(AssertionError):
            calc(figure, function, size)

    def test_invalid_size(self):
        """Тест calc для некорректного размера аргументов."""
        # Arrange
        figure = 'circle'
        function = 'area'
        size = [3, 4]

        # Act & Assert
        with self.assertRaises(TypeError):
            calc(figure, function, size)


if __name__ == "__main__":
    unittest.main()
