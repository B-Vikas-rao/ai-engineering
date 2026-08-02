a = int(input("Enter marks: "))

try:
    if a < 0 or a > 100:
        raise Exception("Invalid Marks")
    print("Marks Accepted")
except Exception as e:
    print(e)