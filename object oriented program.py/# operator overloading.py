# operator overloading 
# operator overloadingintarnally implemented by using magic method

'''class Deposit:                #without using magic method
    def __init__(self,cash):
        self.cash = cash

d1=Deposit(1000)
d2=Deposit(2000)
print(d1+d2)'''

# magic method available for every operator to overload any operator we have to override that method in our class.
# the __add__method is a magic method which gets called when we add 2 numbersusing the + operator.

'''class Deposit:
    def __init__(self,cash):
        self.cash = cash
    
    def __add__(self,others):  #magic method
        return self.cash + others.cash

d1=Deposit(1000)
d2=Deposit(2000)
print("total cash deposit amount=",d1+d2)'''


'''
 - ==> object.__sub__(self,other)
 * ==> object.__mul__(self,other)
 / ==> object.__div__(self,other)
 // ==> object.__floordiv__(self,other)
 % ==> object.__mod__(self,other)
 ** ==> object.__pow__(self,other)
 += ==> object.__iadd__(self,other)
 -= ==> object.__isub__(self,other)
 *= ==> object.__imul__(self,other)
 /= ==> object.__idiv__(self,other)
 //= ==> object.__ifloordiv__(self,other)
 %= ==> object.__imod__(self,other)
 **= ==> object.__ipow__(self,other)
 < ==> object.__lt__(self,other)
 <= ==> object.__le__(self,other)
 > ==> object.__gt__(self,other)
 >= ==> object.__ge__(self,other)
'''