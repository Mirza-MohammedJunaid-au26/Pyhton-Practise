# 1) Write a program to print “hello world” n times, take n as input from the user.

# Ans :

# user_input = int(input("Enter Number : "))

# for i in range(1,user_input+1):
#     print("Hello World")



# 2) Write a program to print n powers of 2, take n as input from the user. 

# Ans :

power_input = int(input("Enter Power : "))
ans = 2
for i in range(1,power_input+1):
   if i%2==0:
       sum = sum*i*power_input
       continue
   elif i%2==1:
        sum = sum*i*power_input
        continue
       


# 3) FizzBuzz - take n as input from the user, From 1 to n, print Fizz if a number is divisible by 3, print Fuzz if a number is divisible by 5.
    #print FizzFuzz if a number is divisible by 3 and 5 both

# Ans :

# num = int(input("Enter Number : "))

# for i in range(1,num+1):
#     if i%3==0 and i%5==0:
#         print("FizzFuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Fuzz")