def sum_n(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s
n = int(input("Enter a number: "))
print("Sum =", sum_n(n))