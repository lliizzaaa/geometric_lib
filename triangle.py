def area(a, b, c):
    '''Принимает числа a, b, c, возвращает половину их суммы'''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны треугольника не могут быть отрицательными")
    return (a + b + c) / 2

def perimeter(a, b, c):
    '''Принимает числа a, b, c, возвращает их сумму'''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны треугольника не могут быть отрицательными")
    return a + b + c
