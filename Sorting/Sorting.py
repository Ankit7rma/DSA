def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break


# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")


# ----------------------------------------------------
# Selection Sort
import sys 
A = [64, 25, 12, 22, 11] 
  
def selectionSort(arr):
# Traverse through all array elements 
    for i in range(len(A)): 
        
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
                
        # Swap the found minimum element with  
        # the first element         
        A[i], A[min_idx] = A[min_idx], A[i] 
  
# Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i],end=" , ")  

# Insertion Sort 
def insertionSort(arr):
    n = len(arr)
    for i in range(n-1):
        j = i+1
        while j>0:
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1] = arr[j-1] , arr[j]
            else:
                break 
            j-=1



# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])


# Cyclic Sort 

def cyclicSort(arr):
    i = 0
    while i<len(arr):
        correctIndex = arr[i]-1
        if arr[i] != arr[correctIndex]:
            arr[i] , arr[correctIndex] = arr[correctIndex],arr[i]
        else:
             i+=1

# Driver code to test above
arr = [5,4,2,1,3]
 
cyclicSort(arr)
print(arr)




