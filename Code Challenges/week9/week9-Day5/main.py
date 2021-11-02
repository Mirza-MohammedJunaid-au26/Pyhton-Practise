# Q.1)

def Smallest(arr):

    for i in range(len(arr)):
        if i > 0:
            if arr[i] > arr[i-1]:
                print(arr[i-1],end=" ")
            else:
                print(-1,end=" ")
        else:
            print(-1,end=" ")
    print()

arr = [2, 3, 4, 5, 1]
Smallest(arr)

# Q.2)

class MinStack():

    stack = []
    stack_len = int(input("Enter Length of Stack :"))-1

    def __init__(self):



        print("!!! Welcome to Min Stack !!!")
        print("1. push")
        print("2. pop")
        print("3. top")
        print("4. Minimum Value")
        print("5. Exit")
        inp = int(input("Enter :"))

        if inp == 1:
            self.Push()
        elif inp == 2:
            self.Pop()
        elif inp == 3:
            self.Top()
        elif inp == 4:
            self.GetMin()
        elif inp == 5:
            print("!!! Thank You !!!")
        else:
            print("Error : Enter Valid Input")
            self.__init__()
            
    def Push(self):

        print("1.Enter Value")
        print("2. Exit")
        inp = int(input("Enter :"))
        
        if inp == 1:
            if len(self.stack) <= self.stack_len:
                push_inp = int(input("Enter :"))
                self.stack.append(push_inp)
                print(self.stack)
                self.Push()
            else:
                print("!!! Overflow !!!")
                self.__init__()
        elif inp == 2:
            self.__init__()

        return self.stack

    def Pop(self):

        print("1.Pop Value")
        print("2. Exit")
        inp = int(input("Enter :"))
        
        if inp == 1:
            if len(self.stack) >= 0:
                self.stack.pop()
                print(self.stack)
                self.Pop()
            else:
                print("!!! Underflow !!!")
                self.__init__()
        elif inp == 2:
            self.__init__()

        return self.stack

    def Top(self):

        print("1.Top Value")
        print("2. Exit")
        inp = int(input("Enter :"))
        
        if inp == 1:
            print(self.stack[-1])
            self.Top()
        elif inp == 2:
            self.__init__()

        return self.stack
    
    def GetMin(self):

        print("1.MinValue")
        print("2. Exit")
        inp = int(input("Enter :"))
        
        if inp == 1:
            print(min(self.stack))
            self.GetMin()

        elif inp == 2:
            self.__init__()

        return self.stack

obj = MinStack()
