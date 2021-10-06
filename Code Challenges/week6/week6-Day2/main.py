#  Q - 1) Explain Abstraction and Polymorphism with example.

# 1) Abstraction: Use to hide Irrevelant Data, Reduce Complexity.

def Abstraction():
    print("Example of Abstraction")

Abstraction()   #Eg of Abstraction

# 2) Polymorphism: Objects And Method have Same name but Different Forms.

# Polymorphism can be Perform through 3 types:
# 1) Object
# 2) Functions
# 3) Method Overriding

# Eg-1) Polymorphism using Object

class HelloWorld:
    def Hello(self):
        print("Hello")
    def World(self):
        print("World")

obj = HelloWorld()
obj.Hello  # same object calling Different Method
obj.World  # same object calling Different Method

# Eg-2) Polymorphism using Functions

def HelloWorld(a):
    print(a)

HelloWorld("Hello")  # same Function passing Different parameters
HelloWorld("World")  # same Function passing Different parameters

# Eg-3) Polymorphism using Method Overriding

class A:
    def Function1(self):
        print("Class A Function-1")
    def Function2(self):
        print("Class A Function-2")
class B(A):
    def Function2(self):
        print("Class B Function-2")
class C(B):
    def Function2(self):
        print("Class C Function-2")

a = A()
b = B()
c = C()

a.Function1()  # Polypmorphism through Method Overriding
a.Function2()  # Polypmorphism through Method Overriding
b.Function1()  # Polypmorphism through Method Overriding
b.Function2()  # Polypmorphism through Method Overriding
c.Function1()  # Polypmorphism through Method Overriding
c.Function2()  # Polypmorphism through Method Overriding


"""
Q – 2) Given the following code:            
 
     N = int(input()) <-- 3
     Sum1 = 0  # 1
     Sum2 = 0  # 1
     For I in range(N): # n+1
          if I%2 == 0:  # 2
              Sum1 += I  # 2 
          else:
              Sum2 += I # 2

     What is the time complexity of the above code ?
"""

# Ans : O(n+12)