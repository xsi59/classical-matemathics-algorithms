import time
import fibonacci as fb

algorithm_selection = int(input("Для выбора алгоритмов вычисления чисел Фибоначчи введите 1: "))
assert ( 0 < algorithm_selection < 2),  'ожидалось целое число в диапазоне от 1 до 1'

if algorithm_selection==1:
    n = int(input("Введите номер числа Фибоначчи для вычисления: "))
    assert (0 <= n < 10001),  'ожидалось целое число в диапазоне от 0 до 997'



def main():
    if algorithm_selection == 1:
        for  foo  in [fb.fibonacci_ver1,fb.fibonacci_ver2,fb.fibonacci_ver3]:
            start_time = time.perf_counter()
            fib_number = foo(n)
            finish_time = time.perf_counter()
            print("Расчетное число=", fib_number, "Время выполнения=", finish_time - start_time, sep=":")



if __name__ == '__main__':
    main()
