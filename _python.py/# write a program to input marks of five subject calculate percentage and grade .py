# write a program to input marks of five subject calculate percentage and grade 

a=float(input("enter marks of physics"))
b=float(input("enter marks of chemistry"))
c=float(input("enter marks of biology"))
d=float(input("enter marks of maths"))
e=float(input("enter marks of computer"))

t=a+b+c+d+e
print("the total is : ",t)
percentage =t/5
if percentage>=90 :
    print("grade A")
elif percentage>=80 :
    print("grade B")
elif percentage>=70 :
    print("grade C")
elif percentage>=60 :
    print("grade D")
elif percentage>=40 :
    print("grade E")
else :
    print("grade F")




