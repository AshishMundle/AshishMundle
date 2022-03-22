# class programs  using constructor 

class hod:
    def __init__(self):      #constructor
        self.name='ashish'
        self.age=19
        self.empid=1001

    def info(self):
        print("my name is :",self.name)
        print("my age is :",self.age)
        print("my emp id :",self.empid)

obj=hod()     #object create 
obj.info()