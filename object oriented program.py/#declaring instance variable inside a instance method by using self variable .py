#declaring instance variable inside a instance method by using self variable 

class student:
    def __init__ (self):
        self.s_name ="prashant"
        self.s_rollno =101
        self.s_branch ="cs"

    def getdata(self):    #instance method
        self.s_mb = 488456565465848

obj=student()          # untill and untiless we call the method it will not added to the object 
obj.getdata()
print(obj.__dict__)