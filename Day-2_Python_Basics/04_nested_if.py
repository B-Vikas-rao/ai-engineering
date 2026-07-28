age = int(input("Enter your age: "))
has_license = bool(input("Do you have a driving license? (True/False): "))
if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a driving license.")
else:
    print("You are too young to drive.")

print("Program Ended")
