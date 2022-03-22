# method overriding using super method 

class Father:
    def bike(self):
        print("bike")

    def laptop(self):
        print("laptop with 2gb ram 500 hdd I3 of parent class")

class Child(Father):
    def laptop(self):
        super().laptop()     # here we are calling parent class method using super()
        print("========================================================")
        print("as per my programming software requirement it is not cool")
        print("laptop with 8gb ram 1 tb hdd I7 is required")

obj = Child()
obj.bike()
obj.laptop()