#  Q1. Write a program to take input from the user and make a list of integers

list1=[]
len_list=int(input("Enter the Length of List : "))
for i in range(1,len_list+1):
    element = int(input("Enter Value : "))
    list1.append(element)
print(list1)


#    Q2. Write a program to convert above list to a tuple

list2 = [8,5,5,6,7,8]
print("Tuple1 =",tuple(list2))


#   Q3. Write a program to remove the 4th last element from a list, and put a string before the 2nd last element 

list3 = [1,2,3,4,5,6,7,8,9]

list3.pop(-4)
print("After Removing 4th last Element : ",list3)
print(list3)
list3.insert(-2,6)
print("After Inserting 2nd last Element : ",list3)
print(list3)



