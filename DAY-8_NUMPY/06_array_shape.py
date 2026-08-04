import numpy as np
a = np.array([1, 2, 3, 4])
print(a.shape)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(c.shape)
print(a.ndim)
print(b.ndim)
print(c.ndim)