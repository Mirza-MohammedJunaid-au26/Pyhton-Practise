# Q.1)

# Without DP

def fib(n):
    
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = 10
print(fib(n))


# with DP
fib = [0]*50

def fibonacci(n):
    
    global fib

    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    if fib[n] > 0:
        return fib[n]
    
    fib1 = fibonacci(n-1)
    fib2 = fibonacci(n-2)

    return fib1 + fib2 

n = 10
print(fibonacci(n))

# Q.2)
pow_list = [0]*20
def pow(b,p):
    
    global pow_list
    if p == 0:
        return 1
    elif p == 1:
        return b
    elif pow_list[p] > 0:
        return pow_list[p]
    
    return b * pow(b,p-1)

print(pow(2,10))

