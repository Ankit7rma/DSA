# # # Return a array of all subsets of the string given 
# def subSets(arr,ansString,string):
#     if string=="":
#         arr.append(ansString)
#         return  
#     ch = string[0]
#     # subSets(arr,ansString,string[1:])
#     # subSets(arr,ansString+ch,string[1:])  this prints ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
#     subSets(arr,ansString+ch,string[1:])
#     subSets(arr,ansString,string[1:])   # this prints ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']

# string = "abc" 
# arr=[] 
# ans = subSets(arr,"",string)

# sorted_arr = sorted(arr, key=lambda x: len(x))
# print(sorted_arr)  #this prints ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'] 
# # print(arr) 

# Return a array of all subsets of the Array given 
# Passing the array from outside 

# def subSetArray(arr,ansArrin,ansArr):
#     if len(arr)==0:
#         ansArr.append(ansArrin.copy())
#         return 
#     item = arr[0]
#     subSetArray(arr[1:],ansArrin +[item],ansArr)
#     subSetArray(arr[1:],ansArrin,ansArr)
    
# arr = [0,1]
# ansArr=[]
# subSetArray(arr,[],ansArr)
# print(ansArr)

# Creating the array inside each call 
# def subSetArray(arr):
#     if len(arr) == 0:
#         return [[]]  # Base case: return a list containing an empty subset
#     else:
#         subsets_without_first = subSetArray(arr[1:])  # Get subsets without the first element
#         subsets_with_first = [[arr[0]] + subset for subset in subsets_without_first]  # Add first element to each subset
#         return subsets_without_first + subsets_with_first  # Combine both subsets

# arr = [0, 1]
# ansArr = subSetArray(arr)
# print(ansArr)

# Iteration 

# def subset(arr):
#     outer = [[]]
#     for num in arr:
#         n = len(outer)
#         for i in range(n):
#             internal = outer[i][:]
#             internal.append(num)
#             outer.append(internal)
#     return outer


# arr = [0, 1,2]
# ansArr = subset(arr)
# print(ansArr)

# #----------Binary Iteration 
# def subSetArray(arr):
#     n = len(arr)
#     subsets = []
#     # Generate subsets using binary representation
#     for i in range(2**n):
#         subset = []
#         for j in range(n):
#             if (i >> j) & 1:
#                 subset.append(arr[j])
#         subsets.append(subset)
#     return subsets

# arr = [0, 1]
# ansArr = subSetArray(arr)
# print(ansArr)
# NExt
# Duplicate Elements are there 
def subsetDuplicate(arr):
    arr.sort()
    outer = [[]]
    start = 0
    end = 0
    for i in range(len(arr)):
        start = 0
        if (i>0 and arr[i]==arr[i-1]):
            start = end+1
        end = len(outer)-1
        n = len(outer)
        for j in range(start,n):
            internal = outer[j][:]
            internal.append(arr[i])
            outer.append(internal)
    return outer

arr = [0, 1,2,2]
ansArr = subsetDuplicate(arr)
print(ansArr)






