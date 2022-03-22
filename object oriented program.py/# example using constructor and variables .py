# example using constructor and variables

class college:
    collegenames="modern college"   # static variable (1 memory)

    def __init__(self):
        self.studentname ="prashant"               # instance variable (3 seprate memory)

principle = college()     # object creation
teacher   = college()
accountant= college()
print("principle=",principle.collegenames,"....",principle.studentname)
print("teacher  =",teacher.collegenames,"....",teacher.studentname)
print("accountant=",accountant.collegenames,"....",accountant.studentname)

college.collegenames="HBD"            # second way to add static variable
principle.studentname="prashant jha"

print("prashant=",principle.collegenames,"|",principle.studentname)
print("teacher =",teacher.collegenames,"|",teacher.studentname)
print("accountant =",accountant.collegenames,"|",accountant.studentname) 