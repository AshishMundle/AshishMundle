# single level inheritance 

class college:  # parent class
    def college_name(self):
        print("modern college")

class student(college):   #child class
    def student_info(self):
        print("name: prashant jha")
        print("branch: mechanical")

obj = student()
obj.college_name()
obj.student_info()