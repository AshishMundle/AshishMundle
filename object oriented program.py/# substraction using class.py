# substraction  using class  

class student:
    roll_number = 101
    num1 = 200
    num2 = 150    #data member 

    def sub(self):   # member function 
        print(self.num1-self.num2)           

obj = student()
obj.sub()
print(obj.roll_number)