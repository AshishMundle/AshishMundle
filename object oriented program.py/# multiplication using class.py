# multiplication using class  
class student:
    roll_number = 101
    num1 = 5
    num2 = 10     #data member 

    def mul(self):   # member function 
        print(self.num1*self.num2)           

obj = student()
obj.mul()
print(obj.roll_number)