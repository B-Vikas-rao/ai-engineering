n = []
m = []
while True:
    print("\n1.Add\n2.Display\n3.Search\n4.Update\n5.Delete\n6.Topper\n7.Average\n8.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        a = input("Enter name: ")
        b = int(input("Enter marks: "))
        n.append(a)
        m.append(b)
    elif ch == 2:
        for i in range(len(n)):
            print(n[i], m[i])
    elif ch == 3:
        a = input("Enter name: ")
        if a in n:
            i = n.index(a)
            print(n[i], m[i])
        else:
            print("Not Found")
    elif ch == 4:
        a = input("Enter name: ")
        if a in n:
            i = n.index(a)
            m[i] = int(input("Enter new marks: "))
        else:
            print("Not Found")
    elif ch == 5:
        a = input("Enter name: ")
        if a in n:
            i = n.index(a)
            n.pop(i)
            m.pop(i)
        else:
            print("Not Found")
    elif ch == 6:
        i = m.index(max(m))
        print(n[i], m[i])
    elif ch == 7:
        print(sum(m) / len(m))
    elif ch == 8:
        break
    else:
        print("Invalid Choice")