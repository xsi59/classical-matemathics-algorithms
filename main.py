import time
import fibonacci as fb
import factorial as fc


print(" Для выбора алгоритмов вычисления чисел Фибоначчи введите  1:\n",
      "Для выбора алгоритмов вычисления факториала числа введите 2:\n",)
algorithm_selection = int(input("Жду ввода:"))
assert ( 0 < algorithm_selection < 3),  'ожидалось целое число в диапазоне от 1 до 2'

if algorithm_selection==1:
    n = int(input("Введите номер числа Фибоначчи для вычисления: "))
    assert (0 <= n < 997),  'ожидалось целое число в диапазоне от 0 до 997'
elif algorithm_selection==2:
    n = int(input("Введите число для вычисления факториала: "))
    assert (0 <= n < 998),  'ожидалось целое число в диапазоне от 0 до 998'



def main():
    if algorithm_selection == 1:
        for  foo  in [fb.fibonacci_ver1,fb.fibonacci_ver2,fb.fibonacci_ver3]:
            start_time = time.perf_counter()
            fib_number = foo(n)
            finish_time = time.perf_counter()
            print("Расчетное число=", fib_number, "Время выполнения=", finish_time - start_time, sep=":")
    elif algorithm_selection == 2:
        for  foo  in [fc.factorial_via_recursion,fc.factorial_through_dynamic_programming]:
            start_time = time.perf_counter()
            fib_number = foo(n)
            finish_time = time.perf_counter()
            print("Расчетное число=", fib_number, "Время выполнения=", finish_time - start_time, sep=":")

if __name__ == '__main__':
    main()
