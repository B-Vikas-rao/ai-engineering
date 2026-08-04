import numpy as np
a=np.array([10,20,30,40])
for i in a:
    print(i)
b=np.array([[1,2],[3,4]])
for i in b:
    print(i)
for i in b:
    for j in i:
        print(j)
c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for i in np.nditer(c):
    print(i)
for i,j in np.ndenumerate(c):
    print(i,j)