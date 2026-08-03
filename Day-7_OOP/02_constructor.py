class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    def show(self):
        print("ID:",self.id)
        print("Name:",self.name)
        print("Marks:",self.marks)
a=int(input("Enter ID: "))
b=input("Enter Name: ")
c=int(input("Enter Marks: "))
d=Student(a,b,c)
d.show()