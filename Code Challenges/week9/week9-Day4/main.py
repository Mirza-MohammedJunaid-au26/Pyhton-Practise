# Q.1) 

def isValid(s):
    opening = "{[("
    closing = "}])"
    brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

s = input("Enter :")
print(isValid(s))

# Q.2) 

def calPoints(ops):

        ans = 0
        history = []
        
        for op in ops:
            if op == "+":
                increment = history[-1] + history[-2]
                history.append(increment)
            elif op == "D":
                increment = history[-1] * 2
                history.append(increment)
            elif op =="C":
                increment = - history.pop()
            else:
                increment = int(op)
                history.append(increment)
                
            ans += increment
        
        return ans

ops = ["5","2","C","D","+"]
print(calPoints(ops))

# Q.3)

def Same_String(s):

    s1 = set(s)
    ans = ''.join(s1)
    print(ans)

st = list(map(str,input()))
Same_String(st) 