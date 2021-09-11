# operators in python 

s='john'
age=22
s1='python'
print ("hello",s,"your age is ",age,"and learning",s1)


age = int( input ('enter your age '))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")


a=int (input ("enter any one number a="))
b=int (input ("enter second number b="))
if a>b :
    print("a is greater")
elif a==b:
    print("a is equal to b")
else: 
    print("b is greater")


n1=int(input ("enter first number: "))
n2=int(input ("enter second number: "))
n3=int(input ("enter third number: "))
if n1>n2 and n1>n3:
    print ("biggest number is: ",n1)
elif n2>n3:
    print ("biggest number is: ",n2)
else :
    print ("biggest number is: ",n3)



# checking number is even or odd

n=int(input("enter any number: "))
if n%2==0:
    print('even no')
else:
    print('odd no')
    