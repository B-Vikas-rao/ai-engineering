f = open("students.txt", "r")

a = f.readlines()

print(len(a))

f.close()