# Bonus Question 

# Ans is option A)

# Derive  the worst case complexity of bubble sort? 
                    # and
# Write a program to perform bubble sort.

# Ans

def bubble(arr):
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
arr = [6,5,4,3,2,1]
print("Bubble Sorting :")
print("Befor Sorting :",arr)
print("After Sorting :",bubble(arr))

# Time Complexity : O(n^2)

print()


# Write a program to perform selection sort.

# Ans :

def selection(arr):
    n  =len(arr)
    for i in range(n-1):
        sm = arr[i]
        idx = i
        for j in range(i+1,n):
            if arr[j] < sm:
                sm = arr[j]
                idx = j
        arr[i],arr[idx] = arr[idx],arr[i]
    return arr

arr = [6,2,1,5,3,4]
print("Selection Sorting :")
print("Before Sorting :",arr)
print("After Sorting :",selection(arr))

# Time Complexity : O(n^2)
