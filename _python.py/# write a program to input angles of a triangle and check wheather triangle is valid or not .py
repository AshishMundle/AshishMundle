# write a program to input angles of a triangle and check wheather triangle is valid or not 

a=int(input("enter the angle a :"))
b=int(input("enter the angle b :"))
c=int(input("enter the angle c :"))
if a+b+c==180 :
    print("the triangle is valid")
else :
    print("the triangle is not valid")
