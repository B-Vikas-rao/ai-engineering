def add(n, r, m1, m2, m3):
    a = input("Enter Name: ")
    b = int(input("Enter Roll Number: "))
    c, d, e = map(int, input("Enter 3 Marks: ").split())
    n.append(a)
    r.append(b)
    m1.append(c)
    m2.append(d)
    m3.append(e)

def display(n, r, m1, m2, m3):
    if len(n) == 0:
        print("No Records")
    else:
        print("\nName\tRoll\tM1\tM2\tM3")
        for i in range(len(n)):
            print(n[i], "\t", r[i], "\t", m1[i], "\t", m2[i], "\t", m3[i])

def search(n, r, m1, m2, m3):
    a = int(input("Enter Roll Number: "))
    if a in r:
        i = r.index(a)
        print(n[i], r[i], m1[i], m2[i], m3[i])
    else:
        print("Student Not Found")

def update(r, m1, m2, m3):
    a = int(input("Enter Roll Number: "))
    if a in r:
        i = r.index(a)
        m1[i], m2[i], m3[i] = map(int, input("Enter New Marks: ").split())
        print("Updated Successfully")
    else:
        print("Student Not Found")

def delete(n, r, m1, m2, m3):
    a = int(input("Enter Roll Number: "))
    if a in r:
        i = r.index(a)
        n.pop(i)
        r.pop(i)
        m1.pop(i)
        m2.pop(i)
        m3.pop(i)
        print("Deleted Successfully")
    else:
        print("Student Not Found")

def average(n, r, m1, m2, m3):
    print("\nName\tAverage")
    for i in range(len(n)):
        a = (m1[i] + m2[i] + m3[i]) / 3
        print(n[i], "\t", a)

def topper(n, r, m1, m2, m3):
    t = []
    for i in range(len(n)):
        t.append(m1[i] + m2[i] + m3[i])
    i = t.index(max(t))
    print("Topper:", n[i], r[i], "Total =", t[i])

def distinction(n, r, m1, m2, m3):
    print("\nStudents Above 75%")
    for i in range(len(n)):
        a = (m1[i] + m2[i] + m3[i]) / 3
        if a >= 75:
            print(n[i], r[i], a)

def failed(n, r, m1, m2, m3):
    print("\nFailed Students")
    for i in range(len(n)):
        a = (m1[i] + m2[i] + m3[i]) / 3
        if a < 35:
            print(n[i], r[i], a)

n = []
r = []
m1 = []
m2 = []
m3 = []

while True:
    print("\n1.Add Student")
    print("2.Display Students")
    print("3.Search Student")
    print("4.Update Marks")
    print("5.Delete Student")
    print("6.Calculate Average")
    print("7.Show Topper")
    print("8.Show Distinction Students")
    print("9.Show Failed Students")
    print("10.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        add(n, r, m1, m2, m3)
    elif ch == 2:
        display(n, r, m1, m2, m3)
    elif ch == 3:
        search(n, r, m1, m2, m3)
    elif ch == 4:
        update(r, m1, m2, m3)
    elif ch == 5:
        delete(n, r, m1, m2, m3)
    elif ch == 6:
        average(n, r, m1, m2, m3)
    elif ch == 7:
        topper(n, r, m1, m2, m3)
    elif ch == 8:
        distinction(n, r, m1, m2, m3)
    elif ch == 9:
        failed(n, r, m1, m2, m3)
    elif ch == 10:
        print("Thank You")
        break
    else:
        print("Invalid Choice")