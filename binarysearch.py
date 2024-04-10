def binarySearch(array, target):
    n = len(array)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1

# Example input
array = [1, 3, 4, 7, 9]  # The array must be sorted for binary search
x = 9

# Call the function
result = binarySearch(array, x)

# Output the result
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found in the array")
