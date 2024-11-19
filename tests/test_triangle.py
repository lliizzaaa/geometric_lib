import unittest
import math
from triangle import area, perimeter

class TestTriangleFunctions(unittest.TestCase):

    def test_area_with_valid_triangle(self):
        a, b, c = 3, 4, 5
        expected_result = 6.0
        result = area(a, b, c)
        self.assertTrue(math.isclose(result, expected_result, rel_tol=1e-9),
                        f"Expected {expected_result}, got {result}")

    def test_area_with_float_triangle(self):
        a, b, c = 2.5, 4.5, 5.5
        p = (a + b + c) / 2
        expected_result = math.sqrt(p * (p - a) * (p - b) * (p - c))
        result = area(a, b, c)
        self.assertTrue(math.isclose(result, expected_result, rel_tol=1e-9),
                        f"Expected {expected_result}, got {result}")

    def test_area_with_negative_side(self):
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError) as context:
            area(a, b, c)
        self.assertEqual(str(context.exception), "Стороны треугольника должны быть положительными")

    def test_area_with_invalid_type(self):
        a, b, c = 3, "side", 5
        with self.assertRaises(ValueError) as context:
            area(a, b, c)
        self.assertEqual(str(context.exception), "Стороны треугольника должны быть числами")

    def test_area_with_invalid_triangle(self):
        a, b, c = 1, 2, 3  # Не может существовать треугольник с такими сторонами
        with self.assertRaises(ValueError) as context:
            area(a, b, c)
        self.assertEqual(str(context.exception), "Сумма любых двух сторон должна быть больше третьей")

    def test_perimeter_with_valid_triangle(self):
        a, b, c = 3, 4, 5
        expected_result = 12
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_result, f"Expected {expected_result}, got {result}")

    def test_perimeter_with_floats(self):
        a, b, c = 2.5, 4.5, 5.5
        expected_result = a + b + c
        result = perimeter(a, b, c)
        self.assertTrue(math.isclose(result, expected_result, rel_tol=1e-9),
                        f"Expected {expected_result}, got {result}")

    def test_perimeter_with_negative_side(self):
        a, b, c = 3, -4, 5
        with self.assertRaises(ValueError) as context:
            perimeter(a, b, c)
        self.assertEqual(str(context.exception), "Стороны треугольника должны быть положительными")

    def test_perimeter_zero(self):
        a, b, c = 0, 0, 0
        with self.assertRaises(ValueError) as context:
            perimeter(a, b, c)
        self.assertEqual(str(context.exception), "Стороны треугольника должны быть положительными")

if __name__ == '__main__':
    unittest.main()
