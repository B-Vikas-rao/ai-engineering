# ===============================
# Student Management System
# ===============================

def line():
    print("-" * 40)


def greet(name="Student"):
    print(f"\nWelcome, {name}!")


def add_marks(*marks):
    return sum(marks)


def reverse_string(text):
    reverse = ""
    for char in text:
        reverse = char + reverse
    return reverse


def palindrome(text):
    return text == reverse_string(text)


name = input("Enter Student Name: ")
age = int(input("Enter Age: "))

greet(name)

if age >= 18:
    print("Eligible for College")
else:
    print("Not Eligible")

line()

while True:

    print("\n===== MENU =====")
    print("1. Display Name")
    print("2. Reverse Name")
    print("3. Check Palindrome")
    print("4. Enter Marks")
    print("5. Print Name Letters")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    match choice:

        case 1:
            print("Student Name:", name)

        case 2:
            print("Reverse:", reverse_string(name))

        case 3:
            if palindrome(name):
                print("Palindrome")
            else:
                print("Not a Palindrome")

        case 4:
            n = int(input("How many marks? "))

            marks = []

            for i in range(n):
                mark = int(input(f"Enter Mark {i+1}: "))
                marks.append(mark)

            total = add_marks(*marks)

            print("Total Marks:", total)
            print("Average:", total / len(marks))

        case 5:

            for letter in name:

                if letter == " ":
                    continue

                print(letter)

        case 6:
            print("Thank You!")
            break

        case _:
            pass
            print("Invalid Choice")

line()
print("Program Ended")