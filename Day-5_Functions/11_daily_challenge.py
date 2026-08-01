from functools import reduce
def show(a):
    for i,j in a.items():
        print(i,j)
try:
    a={}
    n=int(input("Enter number of students: "))
    for i in range(n):
        b=input("Enter name: ")
        c=int(input("Enter marks: "))
        a[b]=c
    print("Original")
    show(a)
    d=list(map(lambda x:x+5,a.values()))
    print("Bonus Marks:",d)
    e=list(filter(lambda x:x>=50,d))
    print("Passed:",e)
    print("Total:",reduce(lambda x,y:x+y,d))
except ValueError:
    print("Invalid Input")
finally:
    print("Program Ended")