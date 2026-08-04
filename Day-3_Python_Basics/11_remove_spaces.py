def remove_space(s):
    r = ""
    for i in s:
        if i != " ":
            r += i
    return r
s = input("Enter a string: ")
print(remove_space(s))