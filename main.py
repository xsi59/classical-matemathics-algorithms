import time


n = int(input("Введите номер числа Фибоначчи для вычисления: "))
assert (0 <= n < 10001),  'ожидалось целое число в диапазоне от 0 до 997'
fib = [None] * 997

def fibonacci_ver1(n: int):
    """ версия 1 Рекурсивная функция расчета n-го числа Фибоначчи
    :rtype: object
    :param n: номер числа, которое нужно вычислить. Целое число от 0 до + бесконечности
    f(20) считалось 0.01с , f(40)  считалось 95с , f(42)  считалось 243с
    """
    if n <= 1:  # крайний случай: для f(0)=0, f(1)=1
        return n
    return fibonacci_ver1(n - 1) + fibonacci_ver1(n - 2)  # реккурентная формула


def fibonacci_ver2(n: int):
    """ версия 2 применение методов динамического программирования для расчета n-го числа Фибоначчи
    :rtype: object
    :param n: номер числа, которое нужно вычислить. Целое число от 0 до + бесконечности
    f(20) считалось 4.13с , f(40)  считалось 5.6с , f(42)  считалось 5.23с
    """
    fib = [None] * (n + 1)
    fib[:2] = [0, 1]
    for k in range(2, n+1):
        fib[k] = fib[k - 1] + fib[k - 2]
    return fib[k]

def fibonacci_ver3(n: int):
    """ версия 3 Рекурсивная функция расчета n-го числа Фибоначчи с кэшированием в список
    :rtype: object
    :param n: номер числа, которое нужно вычислить. Целое число от 0 до + бесконечности
    f(20) считалось 3.41с , f(40)  считалось 4.1с , f(42)  считалось 9.4с
    """

    if fib[n] is not None:  #крайний случай
        return fib[n]
    elif n < 2:
        fib[n] = n
        return fib[n]
    else:
        fib[n] = fibonacci_ver3(n - 1) + fibonacci_ver3(n - 2)
        return fib[n]


def recursion(n: int):
    """Реализация различных алгоритмов для обучения подрастающего поколения"""
    start_time = time.perf_counter()  # засекаем время старта
    fib_number = fibonacci_ver1(n)
    finish_time = time.perf_counter()  # засекаем время финиша
    print("Расчетное число=", fib_number, "Время выполнения=", finish_time - start_time, sep=":")


def dynamic_programming(n: int):
    start_time = time.perf_counter()  # засекаем время старта
    fib_number = fibonacci_ver2(n)
    finish_time = time.perf_counter()  # засекаем время финиша
    print("Расчетное число=", fib_number, "Время выполнения=", finish_time - start_time, sep=":")


def Recursion_with_caching(n: int):
    start_time = time.perf_counter()  # засекаем время старта
    fib_number = fibonacci_ver3(n)
    finish_time = time.perf_counter()  # засекаем время финиша
    print("Расчетное число=", fib_number, "Время выполнения=", finish_time - start_time, sep=":")


def main():
    """ 1- я Реально вычисляет до 42 числа и скорость падает логарифмически
        2-я вычисляет очень большие числа с очень большой скоростью
        3-я начиная где-то с 50-го числа скорость логарифмически растет и обгоняет второй, но орграничено глубиной 996
     """
    recursion(n)
    dynamic_programming(n)
    Recursion_with_caching(n)


if __name__ == '__main__':
    main()
