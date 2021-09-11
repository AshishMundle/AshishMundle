# experimenting default except block 

try:
    a=int(input("enter first integer no "))
    b=int(input("enter second integer no "))
    print(a/b)
except:
    print("this is default exception block")
except (ValueError ,ZeroDivisionError) as message:
    print("enter correct number: ",message)
