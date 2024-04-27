# def permutations(ans,p,up):
#     if len(up)==0:
#         ans.append(p)
#         return ans 
#     ch = up[0]
#     for i in range(len(p)+1):
#         first = p[:i]
#         second =p[i:]
#         permutations(ans,first+ch+second,up[1:])
#     return ans


# answer = permutations([],"","abcd")
# print(answer)
# print(len(answer))



def permutationsCount(ans,p,up):
    if len(up)==0:
        return 1
    ch = up[0]
    count = 0
    for i in range(len(p)+1):
        first = p[:i]
        second =p[i:]
        count +=permutationsCount(ans,first+ch+second,up[1:])
    return count


answer = permutationsCount([],"","abc")
print(answer) 