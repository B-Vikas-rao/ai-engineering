f = open("students.txt", "r")

a = f.read()

print(len(a.split()))

f.close()