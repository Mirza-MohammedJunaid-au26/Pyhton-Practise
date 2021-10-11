# Q - 1 ) Write a code that takes input a string of integers, separated by space, and return a list of integers:

# Ans :

class String_Int:

    def __init__(self):
        self.inp = input("Enter Number :")
        self.list1 = []
        for i in self.inp:
            if i == " ":
                continue
            else:
                inp_i = int(i)
                self.list1.append(inp_i)
        print("List =",self.list1)

# obj = String_Int()


# Q - 2 ) Find largest number in a list, and second largest number, (without using inbuilt functions).

class Biggest:

    def __init__(self):
        A = [1,3,4,5,8,1,2,3,4,9,6,9]
        first_Largest = 0
        second_largest = 0

        for i in A:
            if i - i+1 > 0:
                first_Largest = i
                for j in A:
                    if j < first_Largest and first_Largest-j >= 0 and first_Largest-j <=1:
                        second_largest = j

        print(first_Largest)
        print(second_largest)


obj1 = Biggest()

# Time Complexity -> O(n2) -> n-square


# 3) Print the pattern as per the value of N, where input N is to be taken from console.

class Pattern:

    def __init__(self):
        self.aestrik="*"
        self.dot="."
        self.pattern_inp = int(input("Enter :"))

        for i in range(self.pattern_inp,0,-2):
            for j in range(1,self.pattern_inp+1):
                a=j-i
                if a==0:
                    a = 1
            print(self.aestrik*a,self.dot*i,self.aestrik*a)

        for i in range(0,self.pattern_inp+1,3):
            for j in range(self.pattern_inp,0,-2):
                a = j-1
                if i==0:
                    self.dot="*"
                    i = 1
                else:
                    print(self.aestrik*a,self.dot*i,self.aestrik*a)
                    
        
            
            

obj2 = Pattern()