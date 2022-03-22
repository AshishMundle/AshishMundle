# declaring instance variable inside a constructor by using self variable

class Student:
    def __init__ (self):
        self.s_name ="prashant"
        self.l_name="jha"     #instance variable 
        self.s_rollno=101
        self.s_branch="cs"
        self.s_mb=00000000000

obj = Student()
print(obj.__dict__)