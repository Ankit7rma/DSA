def merge(left,right):
    n = len(left)
    m = len(right)
    i = 0
    j = 0
    k = 0
    mix = [0]*(n+m)
    while i<n and j <m:
        if left[i]<=right[j]:
            mix[k] = left[i]
            i+=1
        else:
            mix[k] = right[j]
            j+=1
        k+=1
    while i <n:
        mix[k] = left[i]
        i+=1
        k+=1
    
    while j <m:
        mix[k] = right[j]
        j+=1
        k+=1
    return mix

def mergeSort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = n//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)


arr = [12, 11, 130, 5, 6, 7] 
sorted_arr = mergeSort(arr)
print(sorted_arr)