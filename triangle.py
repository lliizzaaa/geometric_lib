import math


def area(a, b, c):
    """Вычисляет площадь треугольника по формуле Герона."""
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны треугольника должны быть положительными")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Сумма любых двух сторон должна быть больше третьей")

    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    """Вычисляет периметр треугольника."""
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны треугольника должны быть положительными")

    return a + b + c
