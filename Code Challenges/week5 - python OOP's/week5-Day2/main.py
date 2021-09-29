# Q1. Create a Student class and initialize it with name and roll number. Make methods to :
#    1. Display - It should display all the information of the student.
#    2. setAge - It should assign age to student
#    3. setMarks - It should assign marks to the student.

# Ans :

class Student:
    
    name = "Mirza Mohammed Junaid"
    roll_no = 1

    def Display(self):
        print("Student Name : ",self.name)
        print("Student Roll No :",self.roll_no)   
    
    def setAge(self):
        age = int(input("Enter Student Age :"))
        print("Student Age :",age)

    def setMarks(self):
        marks = int(input("Enter Marks : "))
        print("Student Marks :",marks)

obj = Student()
obj.Display()
obj.setAge()
obj.setMarks()


# Q2. Create a Circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

# Ans :

class Circle:
    
    radius = int(input("Enter Radius : "))

    def getArea(self):
        area_of_circle = 3.14*self.radius*self.radius
        print("Area of Circle is :",area_of_circle)
    
    def getCircumference(self):
        area_of_circle = 2*3.14*self.radius
        print("Circumference of Circle is :",area_of_circle)

obj1 = Circle()
obj1.getArea()
obj1.getCircumference()