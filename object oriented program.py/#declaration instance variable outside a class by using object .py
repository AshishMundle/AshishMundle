#declaration instance variable outside a class by using object 

class student:
    def __init__ (self):
        self.s_name ="prashant"
        self.s_rollno =101

    def getdata(self):   
        self.s_mb = 488456565465848

obj=student()         
obj.getdata()
obj.s_branch ="cs"   # adding instance variable by using object
print(obj.__dict__)
