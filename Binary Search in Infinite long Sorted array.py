# https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/ 



def findPos(arr,target):
    start = 0
    end = 1
    while target>arr[end]:
        temp = end+1
        end = end+ (end-start+1)*2
        start = temp 
    return binarySearch(arr,start,end,target)

def binarySearch(arr,start,end,target):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return -1


# Driver code
if __name__ == '__main__':
    arr = [3, 5, 7,8, 9, 10, 20,90, 100, 130, 140, 160, 170]
    target = 10
    # Function call
    ans = findPos(arr, target)
    if ans == -1:
        print("Element not found")
    else:
        print("Element found at index", ans)