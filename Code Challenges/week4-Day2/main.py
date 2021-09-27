# Q1. What will be the output ?

def printMax(a, b):
   if a > b:
        print(a, 'is maximum')
   elif a == b:
        print(a, 'is equal to', b)
   else:
        print(b, 'is maximum')
printMax(3, 4)

#Ans : 4 is maximum


# Q2. What will be the output ?

x = 50
def func(x):
     print('x is', x)
     x = 2
     print('Changed local x to', x)

func(x)
print('x is now', x)

# Ans : x is 50
#       Changed local x to 2
#       x is now 50



# Q3. Write a function which will take a str as input and will return a string
#     where vowels are removed.

def vowelsRemove(a):
    newString = a;
    vowels = ('a','e','i','o','u')
    for i in a:
        if i in vowels:
            newString = newString.replace(i,"");
    print(newString);

str = input("Enter the String : ")
vowelsRemove(str)