class A:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c
    def display(self):
        print("This is a class A display()")
        print("Value of a is %d"%(self.__a))
        print("Value of b is %d"%(self._b))
        print("value of c is {}".format(self.c))

class B(A):
    def display(self):
        super().display()
        print("This is a class B display()")
        try:
            print("Value of a is %d"%(self.__a))
        except AttributeError: 
            print("YOU CAN'T ACCESS PRIVATE ELEMENTS")
        print("Value of b is %d"%(self._b))
        print(f"value of c is {self.c}")


b=B(40,50,60)
b.display()