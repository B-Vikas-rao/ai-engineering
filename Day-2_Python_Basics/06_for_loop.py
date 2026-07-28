print("===== Example 1: Print Numbers from 1 to 5 =====")
for i in range(1, 6):
    print(i)
print()
print("===== Example 2: Print Even Numbers =====")
for i in range(2, 11, 2):
    print(i)
print()
print("===== Example 3: Countdown =====")
for i in range(5, 0, -1):
    print(i)
print()
print("===== Example 4: Multiplication Table of 5 =====")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print()
print("===== Example 5: Sum of Numbers from 1 to 10 =====")
total = 0
for i in range(1, 11):
    total += i
print("Sum =", total)
print()
print("===== Example 6: Print Characters of a String =====")
name = "Python"
for letter in name:
    print(letter)
print()
print("===== Program Ended =====")
