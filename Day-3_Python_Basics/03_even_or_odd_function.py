def even_odd(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"
a = int(input("Enter a number: "))
print(even_odd(a))