file = open("sample.txt", "w")

file.write("Welcome to Python\n")
file.write("File Handling Example")

file.close()

file = open("sample.txt", "r")

print(file.read())

file.close()