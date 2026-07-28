print("===== break Statement =====")
for i in range(1, 11):
    if i == 6:
        break
    print(i)
print()
print("===== continue Statement =====")
for i in range(1, 11):
    if i == 6:
        continue
    print(i)
print()
print("===== pass Statement =====")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)

print("\nProgram Ended")
