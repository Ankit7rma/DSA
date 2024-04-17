 

def RBS(arr, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    
    if arr[mid] >= arr[start]:
        if target >= arr[start] and target <= arr[mid]:
            return RBS(arr, target, start, mid - 1)
        else:
            return RBS(arr, target, mid + 1, end)
    else:
        if target >= arr[mid] and target <= arr[end]:
            return RBS(arr, target, mid + 1, end)
        else:
            return RBS(arr, target, start, mid - 1)


arr = [23, 43, 54, 67, 0, 1, 3, 4, 5]
ans = RBS(arr, 2, 0, len(arr) - 1)  # Corrected end index
print(ans)
