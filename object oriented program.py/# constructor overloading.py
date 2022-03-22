# constructor overloading

#constructor overloading is not posible in python 
#if we define multiple constructor then the last constructor will be considered

class Arithametic:
    def __init__(self):
        print("there is no argument")
    def __init__(self,a):
        print("pasing one argument")
    def __init__(self,a,b):
        print("passing two arguments")

obj = Arithametic()          # it will give TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
obj = Arithametic(10)
obj = Arithametic(2,3)