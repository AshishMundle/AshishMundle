# addition using class  specially use for printing marksheet 

class student:
    roll_number = 101
    num1 = 50
    num2 = 100     #data member 

    def add(self):   # member function 
        print(self.num1+self.num2)           

obj = student()
obj.add()
print(obj.roll_number)