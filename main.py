import time


def fibonacci_ver1(n: int) -> int:
    """ версия 1 Рекурсивная функция расчета n-го числа Фибоначчи
    :rtype: object
    :param n: номер числа, которое нужно вычислить. Целое число от 0 до + бесконечности
    f(20) считалось 0.01с , f(40)  считалось 95с , f(42)  считалось 243с
    """
    assert n >= 0, 'Ожидается целое положительное число или О'
    if n <= 1:  # крайний случай: для f(0)=0, f(1)=1
        return n
    return fibonacci_ver1(n - 1) + fibonacci_ver1(n - 2)  # реккурентная формула


def fibonacci_ver2(n: int) -> int:
    """ версия 2 применение методов динамического программирования для расчета n-го числа Фибоначчи
    :rtype: object
    :param n: номер числа, которое нужно вычислить. Целое число от 0 до + бесконечности
    f(20) считалось 4.13с , f(40)  считалось 5.6с , f(42)  считалось 5.23с
    """
    assert n >= 0, 'Ожидается целое положительное число или О'
    fib = [None] * (n + 1)
    fib[:2] = [0, 1]
    for k in range(2, n+1):
        fib[k] = fib[k - 2] + fib[k - 1]
    return fib[k]


def recursion():
    """Реализация различных алгоритмов для обучения подрастающего поколения"""
    n = int(input("Введите номер числа Фибоначчи для вычисления: "))
    start_time = time.perf_counter()  # засекаем время старта
    fib_number = fibonacci_ver1(n)
    finish_time = time.perf_counter()  # засекаем время финиша
    print("Расчетное число=", fib_number, "Время выполнения=", finish_time - start_time, sep=":")


def dynamic_programming():
    n = int(input("Введите номер числа Фибоначчи для вычисления: "))
    start_time = time.perf_counter()  # засекаем время старта
    fib_number = fibonacci_ver2(n)
    finish_time = time.perf_counter()  # засекаем время финиша
    print("Расчетное число=", fib_number, "Время выполнения=", finish_time - start_time, sep=":")


def main():
    recursion()
    dynamic_programming()

if __name__ == '__main__':
    main()
