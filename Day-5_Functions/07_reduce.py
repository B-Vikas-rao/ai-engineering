from functools import reduce
a=list(map(int,input("Enter numbers: ").split()))
b=reduce(lambda x,y:x+y,a)
print(b)