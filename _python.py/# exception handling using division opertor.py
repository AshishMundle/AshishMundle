# exception handling using division operator 

#a=int(input("enter first integer no"))
#b=int(input("enter second integer no"))
#multiple except block 
try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except ZeroDivisionError as message :
    print("pls ensure that you can't divide any no by zero:",message)
except ValueError as message:
    print("enter only integer no =>",message)

