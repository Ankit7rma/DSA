# # Return a array of all subsets of the string given 
def subSets(arr,ansString,string):
    if string=="":
        arr.append(ansString)
        return  
    ch = string[0]
    # subSets(arr,ansString,string[1:])
    # subSets(arr,ansString+ch,string[1:])  this prints ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
    subSets(arr,ansString+ch,string[1:])
    subSets(arr,ansString,string[1:])   # this prints ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']


string = "abc" 
arr=[] 
ans = subSets(arr,"",string)

sorted_arr = sorted(arr, key=lambda x: len(x))
print(sorted_arr)  #this prints ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'] 
# print(arr) 
