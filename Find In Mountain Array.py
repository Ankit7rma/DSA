# Definition of the MountainArray class
class MountainArray:
    def __init__(self, array):
        self.array = array

    def get(self, index):
        return self.array[index]

    def length(self):
        return len(self.array)

# Implementation of the Solution class
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findPos(array, n):
            start = 0
            end = n - 1
            while start < end:
                mid = (start + end) // 2
                if array.get(mid) < array.get(mid + 1):
                    start = mid + 1
                else:
                    end = mid
            return start
        
        def search(mountain_arr, target, start, end):
            first_try = binary_search(mountain_arr, target, 0, start)
            if first_try != -1:
                return first_try
            return binary_search(mountain_arr, target, start, end)
        
        def binary_search(mountain_arr, target, start, end):
            is_asc = mountain_arr.get(start) < mountain_arr.get(end)
            while start <= end:
                mid = (start + end) // 2
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                if is_asc:
                    if mid_val > target:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if mid_val < target:
                        end = mid - 1
                    else:
                        start = mid + 1
            return -1

        n = mountain_arr.length()
        pivot = findPos(mountain_arr, n)
        return search(mountain_arr, target, pivot, n - 1)

# Input array and target value
array = [1, 2, 3, 4, 5, 3, 1]
target = 3

# Create an instance of MountainArray
mountain_arr = MountainArray(array)

# Create an instance of the Solution class
solution = Solution()

# Call the findInMountainArray function and print the result
print(solution.findInMountainArray(target, mountain_arr))  # Output: 2
