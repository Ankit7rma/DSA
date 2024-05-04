

# Count No of ways you can reach one end to another going right and down only   
def countWays(r,c):
    if r==1 or c==1:
        return 1
    left = countWays(r-1,c)
    right = countWays(r,c-1)

    return left + right 

# maze is of 3,3 we need to reach from 0,0 to 3,3
ans = countWays(3,3)
print(ans)


# def MazeWaysPrint(p, r, c):
#     if r == 1 and c == 1:
#         print(p)  # Print the path when reaching the bottom-right corner
#         return
#     if r > 1:
#         MazeWaysPrint(p + "D", r - 1, c)  # Move down
#     if c > 1:
#         MazeWaysPrint(p + "R", r, c - 1)  # Move right

# MazeWaysPrint("", 3, 3)


# def MazeWaysPrint(p, r, c):
#     paths = []
#     if r == 1 and c == 1:
#         paths.append(p)  # Append the path when reaching the bottom-right corner
#         return paths
#     if r > 1:
#         down_paths = MazeWaysPrint(p + "D", r - 1, c)  # Move down
#         paths.extend(down_paths)
#     if c > 1:
#         right_paths = MazeWaysPrint(p + "R", r, c - 1)  # Move right
#         paths.extend(right_paths)
#     return paths

# paths = MazeWaysPrint("", 3, 3)
# print(paths)

# def MazeWaysPrinta(p, r, c):
#     paths = []
#     if r == 1 and c == 1:
#         paths.append(p)  # Append the path when reaching the bottom-right corner
#         return paths
#     if r > 1 and c>1:
#         diaPaths = MazeWaysPrinta(p + "D", r - 1, c-1)  # Move down
#         paths.extend(diaPaths)
#     if r > 1:
#         down_paths = MazeWaysPrinta(p + "V", r - 1, c)  # Move down
#         paths.extend(down_paths)
#     if c > 1:
#         right_paths = MazeWaysPrinta(p + "H", r, c - 1)  # Move right
#         paths.extend(right_paths)
#     return paths

# paths = MazeWaysPrinta("", 3, 3)
# print(paths)

# {With Restriction 
# def mazeWithRestrictions(p,maze,r,c):
#     paths = []
    
#     if r == len(maze)-1 and c == len(maze[0])-1:
#         paths.append(p)
#         return paths
#     if (maze[r][c]==False):
#         return paths
#     if r<len(maze)-1:
#         dwn = mazeWithRestrictions(p+"D",maze,r+1,c)
#         paths.extend(dwn)
#     if c<len(maze[0])-1:
#         rth = mazeWithRestrictions(p+"R",maze,r,c+1)
#         paths.extend(rth)

#     return paths
 
# maze = [[True,True,True],[True,False,True],[True,True,True]]
 
# ansArr = mazeWithRestrictions("",maze, 0, 0)
# print(ansArr)  



# def mazeWithRestrictions(ansArr,p,maze,r,c):
     
#     if r == len(maze)-1 and c == len(maze[0])-1:
#         ansArr.append(p)
#         return  
#     if (maze[r][c]==False):
#         return  
#     if r<len(maze)-1:
#         mazeWithRestrictions(ansArr,p+"D",maze,r+1,c)
#     if c<len(maze[0])-1:
#         mazeWithRestrictions(ansArr,p+"R",maze,r,c+1)

     
# ansArr=[]
# maze = [[True,True,True],[True,False,True],[True,True,True]]
# mazeWithRestrictions(ansArr,"",maze, 0, 0)
# print(ansArr) 
# # }