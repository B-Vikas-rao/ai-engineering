def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
while True:
    print("\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 5:
        break
    a, b = map(int, input("Enter two numbers: ").split())
    if ch == 1:
        print(add(a, b))
    elif ch == 2:
        print(sub(a, b))
    elif ch == 3:
        print(mul(a, b))
    elif ch == 4:
        print(div(a, b))
    else:
        print("Invalid Choice")