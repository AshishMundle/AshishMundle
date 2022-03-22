#multiple inheritance 

class subjmarks:     # class-1
    math = int(input("enter paper marks of math"))
    DE = int(input("enter paper marks of designe engineering"))
    c = int(input("enter paper marks of c language"))
    english = int(input("enter paper marks of english"))

        #======================    parent class-1 ============

class practmarks :  # class=2
    cpract = int(input("enter practicals marks of c language"))

        #======================    parent class-2 ============

class Totalmarks(subjmarks,practmarks):   #child class
    #print("if student pass in both = subject and practical paper then pass")
    def total(self):
        if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
            print("pass")
        else:
            print("fail")

obj = Totalmarks()
obj.total()
#print(issubclass(Totalmarks,subjmarks))