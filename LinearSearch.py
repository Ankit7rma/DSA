 
def linearSearch(array, n, x):
    if array.length==0:
        return -1
    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1