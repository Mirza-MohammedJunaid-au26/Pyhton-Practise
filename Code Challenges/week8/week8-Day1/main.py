# Palindrome

palindrome = 0

def pal(n):
    global palindrome
    if n > 0:
        r = n % 10
        palindrome = palindrome * 10 + r
        pal(n // 10)
    return palindrome

inp1 = int(input("Enter a number:"))

num = pal(inp1)
if num == inp1:
    print("Number is palindrome:", inp1)
else:
    print("Number is not palindrome:", inp1)



# Program for Sum of the digits of a given number:

def sum_of_digit(i):
    if i == 0:
        return 0
    return (i % 10 + sum_of_digit(int(i / 10)))
 
inp2 = int(input("Enter :"))
print(sum_of_digit(inp2))


# Given a number n, find sum of first n natural numbers:

def sum(i):
    
    if i == 1:
        return 1
    
    else:
        return i + sum(i-1)

inp = int(input("Enter :"))
print(sum(inp))


# Bonus Question

def pow(b,p):
    
    if p == 1:
        return b
    
    else:
        return b + pow(b,p-1)

inp3 = int(input("Enter Number :"))
inp4 = int(input("Enter Power :"))
print(pow(inp3,inp4))