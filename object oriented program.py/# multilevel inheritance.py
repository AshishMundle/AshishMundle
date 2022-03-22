# multilevel inheritance 

class college:     #first class        first-level
    def college_name(self):
        print("modern college")

class student(college):     #second class      second-level
    def student_info(self):
        print("name: prashant jha")
        print("branch: mechanical")

class Exam(student):     #child class
    def subject(self):
        print("subject1: designe engineering")
        print("subject2: math")
        print("subject3: c-language")

obj = Exam()
obj.college_name()
obj.student_info()
obj.subject()