# write a program to check weather the triangle is equalitoral ,isoscles or scalene triangle 

a=int(input("enter the length a :"))
b=int(input("enter the length b :"))
c=int(input("enter the length c :"))
if a==b==c and a+b+c==180:
    print("the triangle is equilateral triangle ")
elif a==b<90 and a+b+c==180 :
    print("the triangle is isoscles triangle ")
else :
    print("the triangle is scalene triangle")