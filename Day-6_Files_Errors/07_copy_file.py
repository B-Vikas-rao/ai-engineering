f = open("students.txt", "r")

a = f.read()

f.close()

g = open("copy.txt", "w")

g.write(a)

g.close()

print("Copied Successfully")