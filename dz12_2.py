def square_rectangle(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError(f"Все значения должны быть в виде чисел! {a=}, {b=}")
    if a < 0 or b < 0:
        raise ValueError(f"Стороны должны быть положительными! {a=}, {b=}")
    return a * b


def square_rectangle2(a, b):
    return a * b