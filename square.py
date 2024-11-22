
def area(side):
    """Вычисляет площадь квадрата по его стороне."""
    if side < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной")
    return side * side


def perimeter(side):
    """Вычисляет периметр квадрата по его стороне."""
    if side < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной")
    return 4 * side
