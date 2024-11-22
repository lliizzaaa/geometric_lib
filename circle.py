import math

def area(r):
    '''Принимает число r, возвращает число пи умноженное на r квадрат'''
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r

def perimeter(r):
    '''Принимает число r, возвращает число 2 умноженное на пи и на r'''
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r