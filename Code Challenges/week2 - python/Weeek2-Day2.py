# Q-1 )Write a program that takes a floating point number as input and prints its integer part only. 

#Ans :

num1 = float(input("Enter The Float Number : "))
print("The Integer is :",int(num1))


#Q-2 ) Write a simple program to explain(using comments) the working of type() function

#Ans :

#type()  : its return the Datatype of Variable

a = 10
b = "Junaid"
c = 12.5
d = True

print(type(a))  # Hence a is Integer it will return int
print(type(b))  # Hence b is String it will return str
print(type(c))  # Hence c is Float it will return float
print(type(d))  # Hence d is Boolean it will return bool


#Q-3)Write a simple calculator with +, -, *, / support in python Use input() function to take inputs from the user

# Ans :

num1 = int(input("Enter The First Number : "))
num2 = int(input("Enter The Second Number : "))

print("The Addition is : ", num1 + num2)
print("The Subtraction is : ", num1 - num2)
print("The Multiplication is : ", num1 * num2)
print("The Division is : ", num1 / num2)
