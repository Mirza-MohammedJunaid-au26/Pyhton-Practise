# Q1. Create a Student class and initialize it with a name and roll number. create an object of that class in the same file and print name and roll number
                                        # And
# Q2. Write the above code to enter details of 10 students, and take input from the user.

class Student:
    name = "Mirza Mohammed Junaid"
    roll_no = 1
    def __init__(self):
        print("Name :",self.name)
        print("Roll No :",self.roll_no)
        for i in range(1,11):
            name = input("Enter Name :")
            roll_no = int(input("Enter Roll No :"))
            print("Name :",name)
            print("Roll No :",roll_no)

obj = Student()