from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        print("Area:",self.a*self.a)
a=int(input("Enter Side: "))
b=Square(a)
b.area()