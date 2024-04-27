def countWays(r,c):
    if r==1 or c==1:
        return 1
    left = countWays(r-1,c)
    right = countWays(r,c-1)

    return left + right 

# maze is of 3,3 we need to reach from 0,0 to 3,3
ans = countWays(3,3)
print(ans)