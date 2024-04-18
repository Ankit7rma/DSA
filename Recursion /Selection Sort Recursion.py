def SsRec(arr,r,c,max):
    if r==0:
        return 
    if c<r:
        if arr[c]>arr[max]:
            SsRec(arr,r,c+1,c)
        else:
            SsRec(arr,r,c+1,max)
    else:
        temp = arr[max]
        arr[max] = arr[r-1]
        arr[r-1] = temp
        SsRec(arr,r-1,0,0)

arr=[1,4,3,2]
SsRec(arr,len(arr),0,0)
print(arr)


    