# write a program to find maximum between five numbers 

a=int(input("enter number a: "))
b=int(input("enter number b: "))
c=int(input("enter number c: "))
d=int(input("enter number d: "))
e=int(input("enter number e: "))
if a>b and a>c and a>d and a>e:
    print(" the maximum number is ",a)
elif b>a and b>c and b>d and b>e:
    print(" the maximum number is ",b)
elif c>a and c>b and c>d and c>e:
    print(" the maximum number is ",c)
elif d>a and d>b and d>c and d>e:
    print(" the maximum number is ",d)
else  :
    print(" the maximum number is ",e)