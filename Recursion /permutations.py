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



# def permutationsCount(ans,p,up):
#     if len(up)==0:
#         return 1
#     ch = up[0]
#     count = 0
#     for i in range(len(p)+1):
#         first = p[:i]
#         second =p[i:]
#         count +=permutationsCount(ans,first+ch+second,up[1:])
#     return count


# answer = permutationsCount([],"","abc")
# print(answer) 


# Array in every loop 
# def permutations(p,up):
#     arr = []
#     if len(up)==0:
#         arr.append(p)
#         return arr
#     ch = up[0]
#     for i in range(len(p)+1):
#         first = p[:i]
#         second = p[i:]
#         a = permutations(first+ch+second,up[1:])
#         arr.extend(a)

        
#     return arr

# ans = permutations("","abc")
# print(ans)


# Print Number of Permutations 
def permutationsCount(p,up):
    count = 0
    if len(up)==0:
        return 1
    ch = up[0]
    for i in range(len(p)+1):
        first = p[:i]
        second = p[i:]
        a = permutationsCount(first+ch+second,up[1:])
        count+=a
    return count 
ans = permutationsCount("","abc")
print(ans)