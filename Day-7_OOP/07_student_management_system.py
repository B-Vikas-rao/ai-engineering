class Student:
    def __init__(self):
        self.a={}
    def add(self):
        b=int(input("Enter ID: "))
        if b in self.a:
            print("Student Already Exists")
            return
        c=input("Enter Name: ")
        d=int(input("Enter Age: "))
        e=input("Enter Course: ")
        f=int(input("Enter Marks: "))
        self.a[b]=[c,d,e,f]
        print("Student Added")
    def view(self):
        if len(self.a)==0:
            print("No Records")
        else:
            for i,j in self.a.items():
                print(i,j)
    def search(self):
        b=int(input("Enter ID: "))
        if b in self.a:
            print(b,self.a[b])
        else:
            print("Student Not Found")
    def update(self):
        b=int(input("Enter ID: "))
        if b in self.a:
            c=input("Enter Name: ")
            d=int(input("Enter Age: "))
            e=input("Enter Course: ")
            f=int(input("Enter Marks: "))
            self.a[b]=[c,d,e,f]
            print("Updated Successfully")
        else:
            print("Student Not Found")
    def delete(self):
        b=int(input("Enter ID: "))
        if b in self.a:
            del self.a[b]
            print("Deleted Successfully")
        else:
            print("Student Not Found")
    def save(self):
        f=open("students.txt","w")
        for i,j in self.a.items():
            f.write(str(i)+","+j[0]+","+str(j[1])+","+j[2]+","+str(j[3])+"\n")
        f.close()
        print("Data Saved")
    def load(self):
        try:
            f=open("students.txt","r")
            self.a={}
            for i in f:
                b=i.strip().split(",")
                self.a[int(b[0])]=[b[1],int(b[2]),b[3],int(b[4])]
            f.close()
            print("Data Loaded")
        except FileNotFoundError:
            print("File Not Found")
a=Student()
while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Save To File")
    print("7.Load From File")
    print("8.Exit")
    try:
        b=int(input("Enter Choice: "))
        if b==1:
            a.add()
        elif b==2:
            a.view()
        elif b==3:
            a.search()
        elif b==4:
            a.update()
        elif b==5:
            a.delete()
        elif b==6:
            a.save()
        elif b==7:
            a.load()
        elif b==8:
            print("Thank You")
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Enter Numbers Only")