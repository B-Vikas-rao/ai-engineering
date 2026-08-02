a = input("Enter text: ")

f = open("students.txt", "a")
f.write("\n" + a)
f.close()

print("Data Appended")