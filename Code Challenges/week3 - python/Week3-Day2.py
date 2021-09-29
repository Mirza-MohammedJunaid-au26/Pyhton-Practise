# Q-1 )Write a program to check if a number is divisible by 4 or not?

# Ans :

inp = int(input("Enter Number :"))

if (inp % 4 == 0):
     print("It is Divisible by 4")
else:
     print("It is Not Divisible by 4")


# Q-2 ) Write a program to check if a number is even or odd?

# Ans :

num = int(input("Enter Number : "))

if(num%2==0):
     print(num,"is Even Number")
else:
     print(num,"is Odd Number")


# Q-3)Write a program to print truth table of OR logical operator 

# Ans :

print("OR Truth Table")
print("condition1     Condition2        Output")
print("  True            True            True")
print("  True            False           True")
print("  False           True            True")
print("  False           False          False")

condition1 = input("Enter Condition1 : ")
condition2 = input("Enter Condition2 : ")

if(condition1=="True" and condition2=="True"):
     print("Output is True")
elif(condition1=="True" and condition2=="False"):
     print("Output is True")
elif(condition1=="False" and condition2=="True"):
     print("Output is True")
elif(condition1=="False" and condition2=="False"):
     print("Output is False")
else:
     print("Enter Valid Number!!!")