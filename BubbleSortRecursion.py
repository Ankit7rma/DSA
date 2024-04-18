def BbSortRec(arr,r,c):
    if r==0:
        return 
    if c<r:
        if arr[c]>arr[c+1]:
            temp = arr[c]
            arr[c] = arr[c+1]
            arr[c+1] =temp
        BbSortRec(arr,r,c+1)
    else:
        BbSortRec(arr,r-1,0)
arr=[1,4,3,2]
ans = BbSortRec(arr,len(arr)-1,0)
print(arr)


    