# Q1. Describe the concepts of Class, Object, Encapsulation and inheritance of OOPS with code examples.

class Base_Class:        # Created a Class

    def __init__(self):      # Constructor
        self._protected = "I am Protected"    # Protected Variable Eg: Encapsulation
        self.__private = "I am Private"       # Private Variable Eg: Encapsulation
        print(self.__private,"I can be Use in Base Class")
        print(self._protected,"I can be Use in Base Class")

class Deriverd_Class(Base_Class):
    
    def __init__(self):      # Constructor    
        Base_Class.__init__(self)
        print(self._protected,"I can also be Use in Derived Class")

obj = Deriverd_Class()  #Object


# Q2. Declare a class Base with attributes x, y where, x is a string and y is an integer. Now declare a class Derived and inherit all the properties of Base. Define a show() method inside Derived class to print x and y. 

class Base:
    def __init__(self):
        self.x = "Mirza Mohammed Junaid"
        self.y = 19

class Derived:

    def __init__(self):
        Base.__init__(self)
        self.show()

    def show(self):
        print("Name : ",self.x)
        print("Age : ",self.y)

obj1 = Derived()