class Queue():

    queue = []
    queue_len = int(input("Enter Length of queue :"))-1

    def __init__(self):

        print("!!! Welcome to Queue !!!")
        print("1. push")
        print("2. pop")
        print("3. peek")
        print("4. Empty or Not")
        print("5. Exit")
        inp = int(input("Enter :"))

        if inp == 1:
            self.Push()
        elif inp == 2:
            self.Pop()
        elif inp == 3:
            self.Peek()
        elif inp == 4:
            self.Empty()
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
            if len(self.queue) <= self.queue_len:
                push_inp = int(input("Enter :"))
                self.queue.append(push_inp)
                print(self.queue)
                self.Push()
            else:
                print("!!! Overflow !!!")
                self.__init__()
        elif inp == 2:
            self.__init__()

        return self.queue

    def Pop(self):

        print("1.Pop Value")
        print("2. Exit")
        inp = int(input("Enter :"))
        
        if inp == 1:
            if len(self.queue) >= 0:
                self.queue.pop(0)
                print(self.queue)
                self.Pop()
            else:
                print("!!! Underflow !!!")
                self.__init__()
        elif inp == 2:
            self.__init__()

        return self.queue

    def Peek(self):

        print("1.Top Value")
        print("2. Exit")
        inp = int(input("Enter :"))
        
        if inp == 1:
            print(self.queue[0])
            self.Peek()
        elif inp == 2:
            self.__init__()

        return self.queue
    
    def Empty(self):
       if len(self.queue) > 0:
          print("Queue is Not Empty")
       else:
          print("Queue is Empty")
       self.__init__()         


obj = Queue()


# Q.2) 
def Rain_Water(height):
   total_water = 0
   for i in range(1, len(height)-1):
      l = max(height[:i])
      r = max(height[i+1:])
      water = min(l, r) - height[i]
      if(water>=0):
         total_water += water
   return total_water

height = [4,2,0,3,2,5]
print("Water Store :",Rain_Water(height))