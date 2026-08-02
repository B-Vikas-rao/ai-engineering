a = input("Enter name: ")
b = input("Enter age: ")
c = input("Enter branch: ")

f = open("students.txt", "w")
f.write(a + "\n")
f.write(b + "\n")
f.write(c)
f.close()

print("Data Written")