def stats(l):
    return sum(l), max(l), min(l), sum(l) / len(l)
l = list(map(int, input("Enter numbers: ").split()))
s, a, b, c = stats(l)
print("Sum =", s)
print("Maximum =", a)
print("Minimum =", b)
print("Average =", c)