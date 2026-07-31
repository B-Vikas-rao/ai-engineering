a = list(map(int, input("Enter elements: ").split()))

print("Original List:", a)

a.append(100)
print("append():", a)

a.extend([200, 300])
print("extend():", a)

a.insert(1, 50)
print("insert():", a)

if 100 in a:
    a.remove(100)
print("remove():", a)

b = a.pop()
print("pop():", a)
print("Popped Element:", b)

print("index():", a.index(50))

print("count():", a.count(50))

a.sort()
print("sort():", a)

a.reverse()
print("reverse():", a)

c = a.copy()
print("copy():", c)

print("len():", len(a))
print("max():", max(a))
print("min():", min(a))
print("sum():", sum(a))

print("sorted():", sorted(a))
print("Original after sorted():", a)

a.clear()
print("clear():", a)