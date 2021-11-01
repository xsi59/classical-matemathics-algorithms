import time  # to calculate the algorithm execution time


def fibonacci_ver1(n:int) ->int:
    """ версия 1 Рекурсивная функция расчета n-го числа Фибоначчи
    :param n: номер числа, которое нужно вычислить. Целое число от 0 до + бесконечности
    f(20) считалось 0.01с , f(40)  считалось 95с , f(42)  считалось 243с
    """
    assert  n >= 0, "Ожидается целое положительное число или О"

    if n <= 1:             # крайний случай: для f(0)=0, f(1)=1
        return n
    return fibonacci_ver1(n - 1) + fibonacci_ver1(n - 2)         # реккурентная формула

def main():
    """Реализация различных алгоритмов для обучения подрастающего поколения"""
    n = int(input("Введите номер числа Фибоначчи для вычисления: "))
    start_time = time.perf_counter()        # засекаем время старта
    fib_number = fibonacci_ver1(n)
    finish_time = time.perf_counter()        # засекаем время финиша
    print("Расчетное число=", fib_number, "Время выполнения=",finish_time-start_time, sep=":")

if __name__ == '__main__':
    main()