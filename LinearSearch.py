 
def linearSearch(array, n, x):
    if len(array)==0:
        return -1
    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

# Example input
array = [3, 7, 1, 9, 4]
n = len(array)
x = 9

# Call the function
result = linearSearch(array, n, x)

# Output the result
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found in the array")