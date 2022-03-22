# class program using parameterize constructor 

class Hod:
    def __init__(self,name,age,rollno):        #parameterize constructor
        self.name = name
        self.age = age
        self.rollno = rollno

    def show(self):
        print('name =',self.name)
        print('age =',self.age)
        print('rollno =',self.rollno)

obj=Hod('prashant',20,101)
obj.show()