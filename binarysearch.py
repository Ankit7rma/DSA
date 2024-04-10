# def binarySearch(array, target):
#     n = len(array)
#     start = 0
#     end = n - 1
#     while start<=end:
#         mid = (start+end)//2
#         if array[mid]<target:
#             start = mid+1
#         elif array[mid]>target:
#             end = mid-1
#         else:
#             return mid
 

# Order Agnostic Binary Search 
def binarySearch(array,target):
    n = len(array)
    start = 0
    end = n-1

    isAsc =  array[start]<array[end]

    while start<= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        
        if isAsc:
            if array[mid]>target:
                end = mid-1
            else:
                start = mid+1
        else:
            if array[mid]<target:
                end = mid-1
            else:
                start = mid+1
        


        


# Example input
array = [1, 3, 4, 7, 9]  # The array must be sorted for binary search
x = 1

# Call the function
result = binarySearch(array, x)

# Output the result
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found in the array")


