
# wap to input basic salary of an employee and calculate its gross salary 

a=float(input("enter black salary :"))
b=float(input("enter HRA :"))
c=float(input("enter DA :"))
 
gr=a+(b*a/100)+(c*a/100)
print("gross salary is ",gr)