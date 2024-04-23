# ----------------CREATING NEW STRING AT EACH CALL

def skipChar(string,k):
  
    if len(string)==0:
        return  ""
    ch = string[0]
    if ch == k:
        return skipChar(string[1:],k)
    else:
        return ch + skipChar(string[1:],k)


string = "bbacdea"
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
  