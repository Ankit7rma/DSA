# ----------------CREATING NEW STRING AT EACH CALL

def skipChar(string,k):
  
    if len(string)==0:
        return  ""
    ch = string[0]
    if ch == k:
        return skipChar(string[1:],k)
    else:
        return ch + skipChar(string[1:],k)


string = "abcapple"
k = "a"
 
ans = skipChar( string,k)
print(ans)


# --------------PASSING STRING IN CALLS
# def skipChar(ans , string,k):
#     if len(string)==0:
#         return ans
#     ch = string[0]
#     if ch == k:
#         return skipChar(ans,string[1:],k)
#     else:
#         return skipChar(ans+ch,string[1:],k)
        
# string = "bbacdea"
# k = "a"
# ans = ""
# ans = skipChar(ans,string,k)
# print(ans)
  


# --------------------apple skip
# def skipApple(string):
  
#     if len(string)==0:
#         return  ""
#     ch = string[0]
#     if string.startswith("apple"):
#         return skipApple(string[5:])
#     else:
#         return ch + skipApple(string[1:])


# string = "bbapplecdea"
 
 
# ans = skipApple( string)
# print(ans)



# ----------Skip app that is not in apple 
# def skipAppNotApple(string):
#     if len(string)==0:
#         return ""
    
#     if string.startswith("app") and not string.startswith("apple"):
#         return skipAppNotApple(string[3:])
#     else:
#         return string[0] + skipAppNotApple(string[1:])
    
    

# string = "bappbapplecdea"
 
 
# ans = skipAppNotApple( string)
# print(ans)


def permutations(ans,p, up):
    if not up:
        ans.append(p)
        return ans
    ch = up[0]
    for i in range(len(p) + 1):
        f = p[:i]
        s = p[i:]
        permutations(ans,f + ch + s, up[1:])
    return ans 
 

ans = permutations([],"", "abc")
print(ans)
 