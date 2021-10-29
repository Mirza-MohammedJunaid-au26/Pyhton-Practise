def Binary_to_Decimal(b):
    decimal = 0
    for i in b:
        decimal = decimal*2 + int(i) 
    
    return decimal

inp = input("Enter Binary No :")
print("Binary :",inp)
print("Decimal :",Binary_to_Decimal(inp))


def Count_one(i):
    count = 0
    for j in range(len(i)):
        if i[j] == "1":
            count = count+1
    
    return count

inp2 = input("Enter :")
print("Number of 1 in given input :",Count_one(inp2))


def OR(a,b):
    
    c = a|b
    return c


inp3 = int(input("Number 1 :"))
inp4 = int(input("Number 2 :"))
print(inp3,"OR",inp4,":",OR(inp3,inp4))