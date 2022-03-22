#method overloading

# method overloading in python is not possible.
# if we are trying to declare multiple method with same name and 
#different number of arguments then python will always cinsider only last method 

'''
class arithmatic :
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)

obj=arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(1,2,3)     # here it gives "TypeError: add() missing 2 required positional arguments: 'b' and 'c'"
'''

# to handel overloading method in python 
# if method  with variable number of arguments required then we can handle with default arguments 

'''
class Arithmatic:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None:
            print(a+b)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)
        else:
            print("enter atleast two argument")

obj=Arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(1,2,3)
'''