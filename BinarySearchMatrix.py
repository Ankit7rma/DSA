def Search(arr,target):
    r = 0
    c = len(arr)
    while r<len(arr) and c >=0:
        if target== arr[r][c]:
            return [r,c]
        if target<arr[r][c]:
            c-=1
        else:
            r+=1
    return -1

arr = [[1 ,2 ,4 ,5],[3 ,4 ,9 ,16],[7 ,10, 14, 29]]
print(Search(arr,9))
