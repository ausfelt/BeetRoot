def fibonacci_search(arr, target):
    # Generate Fibonacci numbers until the first number greater than or equal to the length of the array and n is number
    fib_n_minus2, fib_n_minus1 = 0, 1,
    fib_n = fib_n_minus1 + fib_n_minus2
    while fib_n < len(arr):
        fib_n_minus2, fib_n_minus1 = fib_n_minus1, fib_n
        fib_n = fib_n_minus1 + fib_n_minus2

    offset = -1
    while fib_n > 1:
        index = min(offset + fib_n_minus2, len(arr) - 1)
        if arr[index] < target:
            fib_n, fib_n_minus1 = fib_n_minus1, fib_n_minus2
            fib_n_minus2 = fib_n - fib_n_minus1
            offset = index
        elif arr[index] > target:
            fib_n, fib_n_minus1 = fib_n_minus2, fib_n_minus1 - fib_n_minus2
            fib_n_minus2 = fib_n - fib_n_minus1
        else:
            return index

    if fib_n_minus1 and arr[offset + 1] == target:
        return offset + 1

    return -1


#Sequential search: O(n) worst-case time complexity. This means that in the worst case scenario, where the target
# element is at the end of the array, the algorithm may have to examine all n elements in the array.

#Binary search: O(log n) worst-case time complexity. This means that in the worst case scenario, the algorithm
#will divide the array into half each time, until it has found the target element or the search range has been
# reduced to zero.

#Fibonacci search: O(log n) worst-case time complexity. This means that in the worst case scenario, the algorithm will
# divide the array into segments whose sizes are determined by Fibonacci numbers.
#In terms of worst-case time complexity, binary search and Fibonacci search are both faster than sequential
#search. However, in practice, binary search may perform better than Fibonacci search due to its lower overhead, as
# Fibonacci search requires computing Fibonacci numbers.

#Moreover, Fibonacci search may be preferred when the cost of accessing the elements of the array is relatively
# high compared to the cost of computing Fibonacci numbers. In such cases, the reduced number of element accesses
# may offset the cost of computing Fibonacci numbers, making Fibonacci search faster than binary search.