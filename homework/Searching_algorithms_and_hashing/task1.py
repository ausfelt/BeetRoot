def binary_search(arr, target):
    # Base case: if the array is empty, the target is not found
    if not arr:
        return False

    mid = len(arr) // 2

    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid + 1:], target)