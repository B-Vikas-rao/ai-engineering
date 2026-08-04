import numpy as np
a=np.array([1,2,3,4,5,6])
print(np.array_split(a,3))
b=np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.array_split(b,2))
c=np.array([[1,2,3,4],[5,6,7,8]])
print(np.hsplit(c,2))
d=np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.vsplit(d,2))