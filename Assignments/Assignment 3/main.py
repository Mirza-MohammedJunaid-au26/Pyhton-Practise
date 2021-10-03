#  Q1. Count no occurrences of each number in a list.

list1 = [ 1, 2, 1, 4, 5, 9, 10, 4, 1, 10, 5, 4] 

for i in range(1,len(list1)):
    a=list1.count(i)
    if a==0:
        continue
    else:
        print("The Count of",i,"is",a,"Times")


#  Q2. Print the pattern for a given integer N, where input for N is user taken:

inp = int(input("Enter :"))
a=1
for i in range(inp,0,-1):
    if a<inp+1:
        print(a*".",end="")
    for j in range(1,i):
        print("*",end="")
    a=a+1
    print()


#  Q-3) Create a class speed and add a method to convert speed from Kilometer per hour to meter per second.

class Speed:
    def __init__(self):
        inp = int(input("Enter km/h : "))
        ms = inp*1000/3600
        print(inp,"km/h =",ms,"m/s")

obj = Speed()
