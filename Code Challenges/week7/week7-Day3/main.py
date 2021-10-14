# 1. Let A be an array arranged in descending order. Check whether an element X is present inside A or not using binary search. 

# Ans :

A = [10,9,8,7,6,5,4,3,2,1]
inp = int(input("Enter :"))
st = 0
en = len(A)-1
not_found = 0

while st <= en:
    
    mid = (st+en)//2

    if A[mid] == inp:
        print(A[mid],"found at",mid,"index")
        not_found=1
        break

    if A[mid] > inp:
        st = mid+1
    
    else:
        en = mid-1

if not_found == 0:
    print("Not Found")


# 2. Find First and last Position of Element in Sorted Array

# Ans :

A = [1,2,2,3,4,5,5,6,6,7]
inp = int(input("Enter :"))
st = 0
en = len(A)-1
count1= []
not_found = 0

while st <= en:
    
    mid = (st+en)//2

    if A[mid] == inp:
        not_found=1
        count1.append(mid)
        continue

    if A[mid] < inp:
        st = mid+1
    
    else:
        en = mid-1

if not_found == 0:
    print("Not Found")

print(count1)