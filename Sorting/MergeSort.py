# def merge(left,right):
#     n = len(left)
#     m = len(right)
#     i = 0
#     j = 0
#     k = 0
#     mix = [0]*(n+m)
#     while i<n and j <m:
#         if left[i]<=right[j]:
#             mix[k] = left[i]
#             i+=1
#         else:
#             mix[k] = right[j]
#             j+=1
#         k+=1
#     while i <n:
#         mix[k] = left[i]
#         i+=1
#         k+=1
    
#     while j <m:
#         mix[k] = right[j]
#         j+=1
#         k+=1
#     return mix

# def mergeSort(arr):
#     n = len(arr)
#     if n == 1:
#         return arr
#     mid = n//2
#     left = mergeSort(arr[:mid])
#     right = mergeSort(arr[mid:])
#     return merge(left,right)


# arr = [12, 1901, 130, 5, 6, 7] 
# sorted_arr = mergeSort(arr)
# print(sorted_arr)
# print(arr)


# IN PLACE MERGE SORT 

def mergeInplace(arr,s,mid,e):
 
    i = s
    j = mid
    k = 0
    mix = [0]*(e-s)
    while i<mid and j<e:
        if arr[i]<=arr[j]:
            mix[k] = arr[i]
            i+=1
        else:
            mix[k] = arr[j]
            j+=1
        k+=1
    while i <mid:
        mix[k] = arr[i]
        i+=1
        k+=1
    
    while j <e:
        mix[k] = arr[j]
        j+=1
        k+=1
    for f in range(len(mix)):
        arr[s+f] = mix[f]

def mergeSortInPlace(arr,start,end):
    if start<end-1:
       
        mid = (end+start)//2
        mergeSortInPlace(arr,start,mid)
        mergeSortInPlace(arr,mid,end)

        mergeInplace(arr,start,mid,end)


arr = [12, 1901, 130, 5, 6, 7] 
mergeSortInPlace(arr,0,len(arr))

print(arr)     
 