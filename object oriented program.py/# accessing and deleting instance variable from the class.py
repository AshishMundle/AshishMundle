# accessing and deleting instance variable from the class 

class student:
    def __init__ (self):
        self.s_name ="prashant"
        self.s_rollno =101

    def getdata(self):   
        self.s_mb = 488456565465848

obj =student()
obj.getdata()
obj.s_branch ="cs"        # adding istance variable by using object 
del obj.s_rollno          # deleteing a instance variable 
print(obj.s_name)
print(obj.__dict__)
