import numpy as np
a = np.array([10, 20, 30, 40, 50])
print(a)
print(a[0])
print(a[2])
print(a[-1])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b[0, 0])
print(b[0, 2])
print(b[1, 1])
print(b[1, 2])
c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(c)
print(c[0, 0, 1])
print(c[1, 1, 0])
print(c[1, 0, 1])