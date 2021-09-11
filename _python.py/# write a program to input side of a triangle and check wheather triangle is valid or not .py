# write a program to input side of a triangle and check wheather triangle is valid or not 

a=int(input("enter the length a :"))
b=int(input("enter the length b :"))
c=int(input("enter the length c :"))
if a+b>=c or b+c>=a or a+c>=b:
    print("the triangle is valid")
else :
    print("the triangle is not valid")
