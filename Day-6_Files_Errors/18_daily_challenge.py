while True:

    print("\n1.Add Student")
    print("2.View Students")
    print("3.Exit")

    a = int(input("Enter choice: "))

    if a == 1:

        r = input("Roll No: ")
        n = input("Name: ")
        m = input("Marks: ")

        f = open("students.txt", "a")
        f.write(r + " " + n + " " + m + "\n")
        f.close()

        print("Student Added")

    elif a == 2:

        f = open("students.txt", "r")

        print(f.read())

        f.close()

    elif a == 3:

        print("Thank You")
        break

    else:

        print("Invalid Choice")