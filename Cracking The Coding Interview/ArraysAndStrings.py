# def is_unique2(s):
#     if s is None or len(s) > 26:
#         return False
#     checker = 0
#     for i in s:
#         val = ord(i) - ord("a")
#         if (checker & (1 << val)) > 0:
#             return False
#         checker |= 1 << val
#     return True

# s = "abcb"
# iu = is_unique2(s)
# print(iu)


# Problem: Given two strings, write a method to decide if one is a permutation of other.

# - Sort the Strings And Check equal 
# - make freq of characters and compare 
# - get all permutations and check in them 
# - at making each permutation check it is equal or not 
{
#1 processed and unprocessed method 
# def checkPermutation(a,b):
#     def permHelper(ans,helpStr,a):
#         if len(a)==0:
#             ans.append(helpStr[:])
#             return 
#         ch = a[0]
#         for i in range(len(helpStr)+1):
#             f = helpStr[:i]
#             s = helpStr[i:]
#             permHelper(ans,f+ch+s,a[1:])
#         return ans 

#     arr = []
#     used = a
#     permHelper(arr,"",used)
#     if b in arr:
#         return True
#     else:
#         return False

# a="abc"
# b="bca"
# ans = checkPermutation(a,b)
# print(ans)




#2 Going deep levels and maintaining a index or string and each time removing the used char
# def checkPermutation(a,b):
#     def permHelper(string,arr,helpArr,used):
#         if len(helpArr)==len(string):
#             arr.append("".join(helpArr))
#             return
#         for i in string:
#             if i not in used:
#                 helpArr.append(i)
#                 used.add(i)
#                 permHelper(string,arr,helpArr,used)
#                 helpArr.pop()
#                 used.remove(i)
#         return 
 
#     arr = []
#     string = a
#     permHelper(string,arr,[],set())
#     print(arr)
#     if b in arr:
#         return True
#     else:
#         return False

# a="abc"
# b="bca"
# ans = checkPermutation(a,b)
# print(ans)


# def checkPermutation(a,b):
#     def backtrack_string(s, ind, res):
#         if ind == len(s):
#             res.append(''.join(s))   
#             return

#         for i in range(ind, len(s)):
#             s[i], s[ind] = s[ind], s[i]
#             backtrack_string(s, ind + 1, res)
#             s[i], s[ind] = s[ind], s[i] 
#     arr = []
#     string = a

# backtrack_string(list(string),0,arr)
# print(arr)
# if b in arr:
#     return True
# else:
#     return False

# a="abc"
# b="bca"
# ans = checkPermutation(a,b)
# print(ans)
}

# URLify
#  Problem: Write a method to replace all spaces in a string with '%20 You may
#  * assume that the string has sufficient space at the end to hold the additional
#  * characters, and that you are given the "true" length of the string. (Note: if
#  * implementing in Java, please use a character array so that you can perform
#  * this operation in place.) EXAMPLE Input: "Mr John Smith     ", 13 Output:
#  * "Mr%20John%20Smith"

# def URLify(string,n):
#     s = ""
#     for i in range(n):
#         if string[i]==" ":
#             s+="%20"
#         else:
#             s+=string[i]

#     return s
# string = "Mr John Smith"
# n = len(string)
# print(n)
# ans = URLify(string,n)
# print(ans)



class Urlify:
    def replace_spaces(self, chars: list, length: int) -> str:
        if chars is None:
            return ""
        
        space_count = 0
        # First loop: count spaces within the original length
        for i in range(length):
            if chars[i] == ' ':
                space_count += 1
        
        index = length + space_count * 2 - 1
        # Ensure the list has enough space
        if index + 1 < len(chars):
            chars = chars[:index + 1]
        
        # Second loop: replace spaces from the end
        for i in range(length - 1, -1, -1):
            if chars[i] == ' ':
                chars[index] = '0'
                chars[index - 1] = '2'
                chars[index - 2] = '%'
                index -= 3
            else:
                chars[index] = chars[i]
                index -= 1
        
        return ''.join(chars)

# Example usage
u = Urlify()
chars = list("Mr John Smith       ")  # The extra spaces are to accommodate the replacements
print(u.replace_spaces(chars, 13))  # Output: "Mr%20John%20Smith"
