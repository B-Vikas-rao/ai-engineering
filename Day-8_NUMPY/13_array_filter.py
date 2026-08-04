import numpy as np
a=np.array([10,20,30,40,50])
b=[True,False,True,False,True]
print(a[b])
c=a>25
print(c)
print(a[c])
d=np.array([1,2,3,4,5,6,7,8,9,10])
print(d[d%2==0])
print(d[d>5])
e=d[(d>=3)&(d<=8)]
print(e)