# intruducing class 

class Student:
    roll_number = 101
    num1 = 50
    num2 = 100      #data member 

    def add(self):     #member function 
        print(self.num1+self.num2)

obj = Student()
obj.add()
print(obj.roll_number)
