# method overriding 

class Father:                             # parent class 
    def bike(self):
        print("harley devidson")

    def laptop(self):
        print("lapi with 2gb ram and 500gb hdd I3 processor")

class Aman(Father):                       # child class
    def laptop(self):                  # method overriding
        print("my programiing software requirement this is not cool")
        print("laptop with 8gb ram and 1 tb hdd I7 is needed")

obj=Aman()
obj.bike()
obj.laptop()
