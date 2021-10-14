# Q1. Let A be an array having N integers. Check whether element X is present inside A or not using linear search. 

arr1 = list(map(int,input("Enter Element Array (using space):").split()))
inp1 = int(input("Enter :"))
a=0

for i in range(len(arr1)):
    if arr1[i] == inp1:
        print("Found at",i+1,"position")
        a =1
        break
if a==0:
    print("Not Found") 


# Q2. Let A be an array having N integers. Print the first and last index where element X is present. 

arr2 = list(map(int,input("Enter Element Array (using space):").split()))
inp2 = int(input("Enter :"))
count = []
for i in range(len(arr2)):
    if arr2[i] == inp2:
        count.append(i)
print(count)
for j in range(0,len(count),len(count)-1):
    print("At :",count[j],"index")


# Q3. Let A be an array having N integers. Print the second last index where element X is present.

arr3 = list(map(int,input("Enter Element Array (using space):").split()))
inp3 = int(input("Enter :"))
count1 = []
for i in range(len(arr3)):
    if arr3[i] == inp3:
        count1.append(i)
print(count1)
print("Second Last Index of",inp3,"at",count1[-2],"index")