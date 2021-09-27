# 1) Write a program to find biggest number out of three positive numbers, given by user.

print("!!!Biggest Number Program!!!")

#Ans :
num1 = int(input(" Enter 1st Number : "))
num2 = int(input(" Enter 2nd Number : "))
num3 = int(input(" Enter 3rd Number : "))

if(num1>num2 and num1>num3):
    print(num1," Is Larger than",num2,"and",num3)
elif(num2>num1 and num2>num3):
    print(num2," Is Larger than",num1,"and",num3)
else:
    print(num3," Is Larger than",num1,"and",num2)
    
# 2) Write a program to find second biggest number out of three positive numbers, given by user.

print("!!!Second Biggest Number Program!!!")

#Ans :
number1 = int(input(" Enter 1st Number : "))
number2 = int(input(" Enter 2nd Number : "))
number3 = int(input(" Enter 3rd Number : "))

if((number1>number2 and number1<number3) or (number1<number2 and number1>number3)):
    print(number1,"Is the Second Biggest Number")
elif((number2>number1 and number2<number3) or (number2<number1 and number2>number3)):
    print(number2,"Is the Second Biggest Number")
if((number3>number2 and number3<number1) or (number3<number2 and number3>number1)):
    print(number3,"Is the Second Biggest Number")


# 3) FizzBuzz - if a number is divisible by 3 - print Fizz, if a number is divisible by 5 - print Fuzz,if a number is divisible by both - print Fizz-Buzz.

print("!!!FIZZ-BUZZ Program!!!")

#Ans :
n = int(input("Enter Number : "));

if(n%3==0 and n%5==0):
    print("FIZZ-BUZZ")
elif(n%3==0):
    print("FIZZ")
elif(n%5==0):
    print("FUZZ")