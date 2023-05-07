import asyncio

async def fibonacci(n):
    if n <= 1:
        return n
    else:
        return await fibonacci(n-1) + await fibonacci(n-2)

async def factorial(n):
    if n == 0:
        return 1
    else:
        return n * await factorial(n-1)

async def squares(n):
    return n * n

async def cubes(n):
    return n * n * n

async def calculate_all(n):
    fib = await fibonacci(n)
    fact = await factorial(n)
    sqr = await squares(n)
    cub = await cubes(n)
    return (fib, fact, sqr, cub)

async def main():
    tasks = []
    for n in range(1, 11):
        task = asyncio.create_task(calculate_all(n))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    fibs = [result[0] for result in results]
    facts = [result[1] for result in results]
    sqrs = [result[2] for result in results]
    cubs = [result[3] for result in results]

    print(f"Fibonacci: {fibs}")
    print(f"Factorial: {facts}")
    print(f"Squares: {sqrs}")
    print(f"Cubes: {cubs}")

asyncio.run(main())

import asyncio
import time

async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine ended")

async def main():
    print("Main coroutine started")
    start_time = time.time()
    await my_coroutine()
    end_time = time.time()
    print(f"Main coroutine ended, execution time: {end_time - start_time:.3f} seconds")

asyncio.run(main())