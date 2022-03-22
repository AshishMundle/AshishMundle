# Inheritance program

class Faculty:     #parent class
    def __init__(self,f_name,dpartment, f_id):
        self.f_name = f_name
        self.dpartment = dpartment
        self.f_id = f_id

    def print_info(self):
        print("faculty information =",self.f_name,self.dpartment,self.f_id)

class cse(Faculty):   #child class 
    pass  #no statement
obj = cse("jyoti mam","computer_science",1002)
obj.print_info()