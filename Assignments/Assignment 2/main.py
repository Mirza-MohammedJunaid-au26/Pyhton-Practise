# Q1. Count no occurrences of a word in a list, where the word is given by a user.

count_list =  ["Mirza","Mohd","Hi","Junaid","Hello World","Hi","Junaid","Mirza","Hello World"]

print(count_list)
inp = input("Enter : ")
print("No of Occurence : ",count_list.count(inp))



# Q2. Take input from user items and their quantity. And then print the item with the maximum quantity.

def fruits(f1,fq1,f2,fq2,f3,fq3):
    if fq1>fq2 and fq1>fq3:
        print(f1,":",fq1)
    elif fq2>fq1 and fq2>fq3:
        print(f2,":",fq2)
    else:
        print(f3,":",fq3)

fruit_1 = input("Enter First Fruit Name : ")
fruit_1_quantity = int(input("Enter Quantity : "))
fruit_2 = input("Enter Second Fruit Name : ")
fruit_2_quantity = int(input("Enter Quantity : "))
fruit_3 = input("Enter Third Fruit Name : ")
fruit_3_quantity = int(input("Enter Quantity : "))
fruits(fruit_1,fruit_1_quantity,fruit_2,fruit_2_quantity,fruit_3,fruit_3_quantity)



# Q-3) Define a method that takes a string as a parameter. Insert all the characters of the string into a list. Convert the entire list into a tuple.
#      Return the tuple from the method and print that.

def list_to_tuple(i):
    word = i
    list2=[]
    index=0
    for j in range(1,len(i)+1):
        a=word[index]
        list2.append(a)
        index=index+1
    print("List :",list2)
    tuple1=tuple(list2)
    return tuple1

inp1 = input("Enter String : ")
print("Tuple : ",list_to_tuple(inp1))