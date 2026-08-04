def palindrome(s):
    r = ""
    for i in s:
        r = i + r
    return s == r
s = input("Enter a string: ")
if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")