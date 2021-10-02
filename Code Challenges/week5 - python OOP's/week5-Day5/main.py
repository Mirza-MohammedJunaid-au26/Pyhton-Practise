class Student:
    
    Institute  = "AttainU"   # Class Attributes 

    def __init__(self,Name,Roll,Batch):
        self.name = Name      # Instance Attributes
        self.roll = Roll      # Instance Attributes
        self.batch = Batch    # Instance Attributes
        self.show()
    
    def show(self):
        print("Student Name :",self.name)
        print("Student Roll No :",self.roll)
        print("Student Batch :",self.batch)
        print("Student Institute :",self.Institute)

object1 = Student("Abdul",1,"Bhabha")
object2 = Student("Ram",2,"C V Raman")
object3 = Student("Shyam",3,"Einstein")
