import multiprocessing as mp

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def squares(n):
    return n * n

def cubes(n):
    return n * n * n

def calculate_all(n):
    fib = fibonacci(n)
    fact = factorial(n)
    sqr = squares(n)
    cub = cubes(n)
    return (fib, fact, sqr, cub)

if __name__ == '__main__':
    pool = mp.Pool(processes=4)
    results = pool.map(calculate_all, range(1, 11))
    pool.close()
    pool.join()

    fibs = [result[0] for result in results]
    facts = [result[1] for result in results]
    sqrs = [result[2] for result in results]
    cubs = [result[3] for result in results]

    print(f"Fibonacci: {fibs}")
    print(f"Factorial: {facts}")
    print(f"Squares: {sqrs}")
    print(f"Cubes: {cubs}")


import threading
import time

def my_function():
    print("Function started")
    time.sleep(1)
    print("Function ended")

def main():
    print("Main thread started")
    start_time = time.time()
    threads = []
    for i in range(5):
        t = threading.Thread(target=my_function)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"Main thread ended, execution time: {end_time - start_time:.3f} seconds")

main()