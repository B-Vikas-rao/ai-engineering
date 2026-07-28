text = input("Enter a string: ")

left = 0
right = len(text) - 1

is_palindrome = True

while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")