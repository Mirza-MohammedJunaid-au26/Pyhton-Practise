# Q1. Write a function to print length of a list

# Ans :

list = [1,"Hello World",True,12.5]
print("The Length of the List is : ",len(list))


# Q2. Write a function to print the reverse of a list, pass the list as a parameter

# Ans :

def reverseList(l):
    print("After Reversing : ",l[::-1])

list1 = [1,2,3,4,5]
print("Before Reversing : ",list1)
reverseList(list1)


# Q3. Write a function that returns(not prints) the data-type of the last element in a list 

# Ans :

def returnDataType(list):
    return(type(list2[-1]))

list2 = ["Junaid",False,23.5,10]
returnDataType(list2)
print(returnDataType(list))