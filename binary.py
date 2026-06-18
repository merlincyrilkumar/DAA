def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_val = 23
result = binary_search_iterative(numbers, target_val)
print(f"Element found at index: {result}")