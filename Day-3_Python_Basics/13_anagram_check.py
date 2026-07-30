def anagram(a, b):
    return sorted(a) == sorted(b)
a = input("Enter first string: ")
b = input("Enter second string: ")
if anagram(a, b):
    print("Anagram")
else:
    print("Not Anagram")