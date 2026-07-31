a = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("Nested List:")
print(a)
print("First Row:", a[0])
print("Second Row:", a[1])
print("Third Row:", a[2])
print("First Element:", a[0][0])
print("Middle Element:", a[1][1])
print("Last Element:", a[2][2])
print("Rows:")
for i in a:
    print(i)
print("Elements:")
for i in a:
    for j in i:
        print(j, end=" ")