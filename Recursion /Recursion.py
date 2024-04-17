
# def findIndexallList(arr,target,index,list):
#     if len(arr)==index:
#         return list
#     if arr[index] == target:
#         list.append(index)
#     return findIndexall(arr,target,index+1,list)
    
def findIndexAll(arr,target,index):
    list = []
    if index == len(arr):
        return list
    if arr[index]==target:
        list.append(index)
    ansfromcalls = findIndexAll(arr,target,index+1)
    list.extend(ansfromcalls)
    return list


arr = [1,2,3,4,5,4,5,6]
# list=[]
ans = findIndexAll(arr,4,0)
print(ans)