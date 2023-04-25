import time

def task_that_runs_quickly():
    print("task 1 is starting")
    for _ in range(10**8*2):
        pass
    print("task 1 just completed")