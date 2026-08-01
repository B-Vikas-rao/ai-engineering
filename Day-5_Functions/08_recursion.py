def f(a):
    if a==0 or a==1:
        return 1
    return a*f(a-1)
a=int(input("Enter number: "))
print(f(a))