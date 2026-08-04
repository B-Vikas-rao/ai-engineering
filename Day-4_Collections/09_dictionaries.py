a={}
n=int(input("Enter number of items: "))
for i in range(n):
    k=input("Enter key: ")
    v=input("Enter value: ")
    a[k]=v
print("Dictionary:",a)
print("Keys:",a.keys())
print("Values:",a.values())
print("Items:",a.items())
for i,j in a.items():
    print(i,j)





    