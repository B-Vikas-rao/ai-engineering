try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except Exception:
    print("Something Went Wrong")
finally:
    print("Program Finished")