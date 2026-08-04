import numpy as np
a=np.array([10,20,30,40])
b=a.copy()
c=a.view()
a[0]=100
print(a)
print(b)
print(c)
c[1]=200
print(a)
print(b)
print(c)
print(a.base)
print(b.base)
print(c.base)