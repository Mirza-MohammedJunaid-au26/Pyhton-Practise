# Q.2 

def left_to_right(num,l):
    if l == 0:
        return num[0]
    else:
        print(num[l])
        return left_to_right(num,l-1)
inp = input("Enter :")
a= len(inp)-1
print(left_to_right(inp,a))

#  Q.3

def reverse(num,l):
    if l == 0:
        return num[0]
    else:
        print(num[l],end="")
        return left_to_right(num,l-1)
inp1 = input("Enter :")
a1= len(inp)-1
print(reverse(inp1,a1))
