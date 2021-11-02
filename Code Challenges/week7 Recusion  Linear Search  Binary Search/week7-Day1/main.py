# Q - 1) Write a program to print the sum of right diagonal of a matrix:

# Q-1.1

#           1  2  3  
# Matrix =  4  5  6
#           7  8  9

# Ans :

arr1 = [[1,2,3],[4,5,6],[7,8,9]]

n=3
for i in range(n):
    print(arr1[i][n-i-1])

print()
# Q-1.2

#           1   2   3    4  
# Matrix =  5   6   7    8
#           9  10   11  12

# Ans :

arr2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

m=3
for i in range(m):
    print(arr2[i][m-i])

print()
# Q-1.3

#           1  2    
# Matrix =  3  4
#           5  6

# Ans :
arr3 = [[1,2],[3,4],[5,6]]
o=1
for i in range(o+1):
    print(arr3[i][o-i])


print()

# Q-2) Write a program to print sum of border elements of a square Matrix

arr4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# My Borders are : 1,2,3,4,5,8,9,12,13,14,15,16

p = 4
q = 4

sum1=0
sum2=0
sum3=0
sum4=0
for i in range(p):
    for j in range(q):
        if (i == 0):
            sum1=sum1+arr4[i][j]
        elif (i == p-1):
            sum2=sum2+arr4[i][j]
        elif (j == 0):
            sum3=sum3+arr4[i][j]
        elif (j == q-1):
            sum4=sum4+arr4[i][j]

print("The Sum of Boundary is :",sum1+sum2+sum3+sum4)

print()

# Q - 3) Write a function to return sum of rows of a matrix as a list:

row_sum = 0
list1 = []
for i in range(p):
    for j in range(q):
        row_sum= row_sum+arr4[i][j]
    list1.append(row_sum)
    row_sum = 0
print("The Sum of the Row is :",list1)
