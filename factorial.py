def factorial_via_recursion(n: int):
    """ версия 1 Рекурсивная функция n!
    f(20) считалось 2.21с , f(40)  считалось 3.70с , f(42)  считалось 3.67с
    """
    if n == 1:
        return 1
    else:
        return factorial_via_recursion(n - 1) * n


def factorial_through_dynamic_programming(n: int):
    """ версия 2 вычисление n! методом динамического программирования
    f(20) считалось 2.58с , f(40)  считалось 3.67с , f(42)  считалось 3.74с
    """
    fac = [1] + [None] * n
    for i in range(1, n+1):
        fac[i] = fac[i - 1] * i
    return fac[i]
