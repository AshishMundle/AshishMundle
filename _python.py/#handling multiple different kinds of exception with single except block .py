# handling multiple different kinds of exception with single except block 

try:
    a=int(input("enter first integer no "))
    b=int(input("enter second integer no "))
    print(a/b)
except (ValueError ,ZeroDivisionError) as message:
    print("enter correct number: ",message)