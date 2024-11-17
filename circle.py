import math


def area(r):
    """Вычисляет площадь круга по радиусу r."""
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r


def perimeter(r):
    """Вычисляет периметр круга (длину окружности) по радиусу r."""
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r
