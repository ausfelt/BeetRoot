import concurrent.futures
import math

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def sequential():
    prime_numbers = []
    for number in NUMBERS:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

def concurrent_threaded():
    prime_numbers = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(is_prime, number) for number in NUMBERS]
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            if future.result():
                prime_numbers.append(NUMBERS[i])
    return prime_numbers

def concurrent_process():
    prime_numbers = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(is_prime, number) for number in NUMBERS]
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            if future.result():
                prime_numbers.append(NUMBERS[i])
    return prime_numbers

if __name__ == '__main__':
    print("Sequential:", sequential())
    print("Concurrent Threaded:", concurrent_threaded())
    print("Concurrent Process:", concurrent_process())

#Concurrent process was significantly faster than the other two. I think this is because the process is running in
#parallel with the other processes, while the threads are running in parallel with the other threads.
#The process is also running on a different core, which is faster than the threads.