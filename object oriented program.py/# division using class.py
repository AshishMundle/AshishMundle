# division using class  

class student:
    roll_number = 101
    num1 = 50
    num2 = 5     #data member 

    def div(self):   # member function 
        print(self.num1/self.num2)           

obj = student()
obj.div()
print(obj.roll_number)