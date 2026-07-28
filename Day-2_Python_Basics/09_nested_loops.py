rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

print("\nPattern:\n")

for i in range(rows):
    for j in range(columns):
        print("*", end=" ")
    print()
