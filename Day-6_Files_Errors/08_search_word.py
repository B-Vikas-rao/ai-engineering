a = input("Enter word: ")

f = open("students.txt", "r")

for i in f:
    if a in i:
        print(i)

f.close()