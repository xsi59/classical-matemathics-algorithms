from multiprocessing import Process, Queue
import os
import time


final_fibonacci_number = 5

def worker(task: int, process_index: int):
    """
    Параллельное программирование на Питоне для числа 40 будет запускатся 40 процессов
    рекурсия
    вычисление N-нного числа Фибоначчи
    """
    def fib(n: int) -> int:          # функцию пишем прямо здесь
        return fib(n - 1) + fib(n - 2) if n > 2 else 1         # реккурентная формула
    number = task
    answer = fib(number)
    print(f"worker {process_index}, PID = {os.getpid()}, fib({number}) = {answer}")

def fibonacci_ver5(n: int):
    tasks = []      #  создаем пустой список
    for n in range(0, final_fibonacci_number + 1):
        tasks.append(n)

    workers = []    # процессы которые будут создаватся
    for process_index in range(final_fibonacci_number + 1):
        worker_process = Process(target=worker, args=(tasks[process_index], process_index,))   # worker здесь функция
        workers.append(worker_process)
    start_time = time.perf_counter()        # засекаем время старта
    for workers_process in workers:
        workers_process.start()
    print("Parent process started")
    for workers_process in workers:
        workers_process.join()
    finish_time = time.perf_counter()  # засекаем время финиша
    print("Parent process jonied Duration:", finish_time-start_time)

if __name__ == '__main__':
    fibonacci_ver5(final_fibonacci_number)