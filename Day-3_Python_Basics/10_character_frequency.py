def frequency(s):
    for i in s:
        print(i, "=", s.count(i))
s = input("Enter a string: ")
frequency(s)