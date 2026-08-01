a=list(map(int,input("Enter numbers: ").split()))
b=list(filter(lambda x:x%2==0,a))
print(b)