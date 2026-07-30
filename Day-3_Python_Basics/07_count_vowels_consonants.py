def count(s):
    v = 0
    c = 0
    for i in s.lower():
        if i.isalpha():
            if i in "aeiou":
                v += 1
            else:
                c += 1

    return v, c
s = input("Enter a string: ")
v, c = count(s)
print("Vowels =", v)
print("Consonants =", c)