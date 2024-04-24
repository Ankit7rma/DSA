# # Return a array of all subsets of the string given 
def subSets(arr,ansString,string):
    if string=="":
        arr.append(ansString)
        return  
    ch = string[0]
    subSets(arr,ansString+ch,string[1:])
    subSets(arr,ansString,string[1:])

string = "abc" 
arr=[] 
ans = subSets(arr,"",string)

sorted_arr = sorted(arr, key=lambda x: len(x))
print(sorted_arr) 
