def second_large(l):
    l = list(set(l))
    l.sort()
    return l[-2]
l = list(map(int, input("Enter numbers: ").split()))
print("Second Largest =", second_large(l))