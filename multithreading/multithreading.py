import threading
import time
import timeit


def task_that_runs_quickly():
    print("task 1 is starting")
    for _ in range(10**8*2):
        pass
    print("task 1 just completed")


def task_that_runs_longer():
    print("task 2 is starting")
    for _ in range(10**8*3):
        pass
    print("task 2 just completed")


print("quicker task measured")
print(timeit.timeit(task_that_runs_quickly, number=1))
print("longer task measured")
print(timeit.timeit(task_that_runs_longer, number=1))

thread_1 = threading.Thread(name="3 seconds", target=task_that_runs_quickly)
thread_2 = threading.Thread(name="5 seconds", target=task_that_runs_longer)


start_time = time.time()
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
end_time = time.time()

execution_time = end_time - start_time
print(f"threads execution time: {execution_time}")