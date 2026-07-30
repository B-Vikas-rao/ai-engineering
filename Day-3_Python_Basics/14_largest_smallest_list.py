def large_small(l):
    return max(l), min(l)
l = list(map(int, input("Enter numbers: ").split()))
a, b = large_small(l)
print("Largest =", a)
print("Smallest =", b)