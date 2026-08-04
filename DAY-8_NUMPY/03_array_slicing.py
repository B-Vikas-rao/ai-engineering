import numpy as np
a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(a[1:5])
print(a[2:])
print(a[:4])
print(a[-4:])
print(a[::2])
print(a[::-1])
b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(b[0:2, 1:3])
print(b[:, 1])
print(b[1, :])
print(b[::2, ::2])