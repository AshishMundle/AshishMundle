# write a program to input electricty unit charges and callculate total bill 

a=float(input("enter the unit :"))
if a<=50 :
    b=a*0.50  
if a<150 :
    b=a*0.75
if a<250 :
    b=a*1.20
if a>251 :
    b=a*1.50
c=b+20*b/100
print("bill =",c)

