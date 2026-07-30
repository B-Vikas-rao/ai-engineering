def reverse(l):
    r = []
    for i in l:
        r = [i] + r
    return r
l = list(map(int, input("Enter numbers: ").split()))
print(reverse(l))