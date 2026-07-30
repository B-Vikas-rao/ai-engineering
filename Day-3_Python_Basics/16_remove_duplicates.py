def remove_duplicate(l):
    r = []
    for i in l:
        if i not in r:
            r.append(i)
    return r
l = list(map(int, input("Enter numbers: ").split()))
print(remove_duplicate(l))