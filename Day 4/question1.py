class Student:
    def __init__(self):
        self.name =""
        self.roll_number =0
        self.marks1=0
        self.marks2=0
        self.marks3=0

    def get_data(self):
     self.name = input("Enter the name:")
     self.roll_number = int(input("Enter the roll number:"))
     self.marks1 = float(input("Enter the marks of maths:"))
     self.marks2 = float(input("Enter the marks of science:"))
     self.marks3 = float(input("Enter the marks of english:"))

    def displaydata(self):
     print("Academic status of student")
     print("Name:",self.name)
     print("Enter the roll number:",self.roll_number)
     print("Enter marks of math:",self.marks1)
     print("Enter marks of science:",self.marks2)
     print("Enter marks of english:",self.marks3)
    def calculate_percentage(self):
     percentage = (self.marks1+self.marks2+self.marks3)/3
     print("Percentage:",percentage)
     
s1 = Student()
s1.get_data()
s1.displaydata()
s1.calculate_percentage()

 

#
