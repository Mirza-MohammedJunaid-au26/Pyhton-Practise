# Q - 1 ) Write a program to find the upper bound (last occurrence’s index) of a target given by the user, that should be present in the list. Using linear search.

A= [1,1,1,2,2,2,3,3,4]
inp = int(input("Enter :"))
i = 0

while i<len(A):
    if A[i] == inp:
        if A[i] == A[i+1]:
            i = i+1
            continue
        else:
            print("The Upper Bound of",inp,"is",i)
    i=i+1

# Time Complexity : O(n)
