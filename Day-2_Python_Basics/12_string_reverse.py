text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

print("\nOriginal String:", text)
print("Reversed String:", reverse)