# def mazeInAllDirections(ansArr,p,maze, r, c):
    
#     if r== len(maze)-1 and c == len(maze[0])-1:
#         ansArr.append(p)
#         return 
#     if(maze[r][c]==False):
#         return 
#     # make changes 
#     maze[r][c]=False
#     if r<len(maze)-1:
#         mazeInAllDirections(ansArr,p+"D",maze,r+1,c)
#     if c<len(maze[0])-1:
#         mazeInAllDirections(ansArr,p+"R",maze,r,c+1)
#     if r>0:
#         mazeInAllDirections(ansArr,p+"U",maze,r-1,c)

#     if c>0:
#         mazeInAllDirections(ansArr,p+"L",maze,r,c-1)
#     # Recover all the changes that are made 
#     maze[r][c]= True
#     return ansArr

     
# ansArr=[]
# maze = [[True,True,True],[True,True,True],[True,True,True]]
# mazeInAllDirections(ansArr,"",maze, 0, 0)
# print(ansArr)
# print(len(ansArr))    


def mazeInAllDirections(ansArr,p,maze, r, c,path,step):
    
    if r== len(maze)-1 and c == len(maze[0])-1:
        path[r][c]=step
        for i in path:
            print(i)
        print(p)
        # print()
        ansArr.append(p)
         
        return 
    if(maze[r][c]==False):
        return 
    # make changes 
    maze[r][c]=False
    path[r][c]=step
    if r<len(maze)-1:
        mazeInAllDirections(ansArr,p+"D",maze,r+1,c,path,step+1)
    if c<len(maze[0])-1:
        mazeInAllDirections(ansArr,p+"R",maze,r,c+1,path,step+1)
    if r>0:
        mazeInAllDirections(ansArr,p+"U",maze,r-1,c,path,step+1)

    if c>0:
        mazeInAllDirections(ansArr,p+"L",maze,r,c-1,path,step+1)
    # Recover all the changes that are made 
    maze[r][c]= True
    path[r][c]=0
    return  ansArr 
     
ansArr=[]
maze = [[True,True,True],[True,True,True],[True,True,True]]
n = len(maze)
m = len(maze[0])
path=  [[0] * m for _ in range(n)]
mazeInAllDirections(ansArr,"",maze, 0, 0,path,step=1)
 
print(ansArr)  
 