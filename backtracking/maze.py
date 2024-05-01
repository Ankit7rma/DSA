# def countWays(r,c):
#     if r==1 or c==1:
#         return 1
#     left = countWays(r-1,c)
#     right = countWays(r,c-1)

#     return left + right 

# # maze is of 3,3 we need to reach from 0,0 to 3,3
# ans = countWays(3,3)
# print(ans)


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

def MazeWaysPrint(p, r, c):
    paths = []
    if r == 1 and c == 1:
        paths.append(p)  # Append the path when reaching the bottom-right corner
        return paths
    if r > 1 and c>1:
        diaPaths = MazeWaysPrint(p + "D", r - 1, c-1)  # Move down
        paths.extend(diaPaths)
    if r > 1:
        down_paths = MazeWaysPrint(p + "V", r - 1, c)  # Move down
        paths.extend(down_paths)
    if c > 1:
        right_paths = MazeWaysPrint(p + "H", r, c - 1)  # Move right
        paths.extend(right_paths)
    return paths

paths = MazeWaysPrint("", 3, 3)
print(paths)
