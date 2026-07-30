def reverse(s):
    r = ""
    for i in s:
        r = i + r
    return r
s = input("Enter a string: ")
print(reverse(s))