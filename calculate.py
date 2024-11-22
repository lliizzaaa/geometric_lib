# src/calc.py

import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1
}


def calc(fig, func, size):
    """Валидирует входные данные и возвращает результат расчётов."""
    assert fig in figs, "Фигура не поддерживается"
    assert func in funcs, "Функция не поддерживается"

    result = eval(f'{fig}.{func}(*{size})')
    return f'{func} of {fig} is {result}', result
