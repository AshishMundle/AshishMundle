#finding factorial using recursive function  

def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result

print("factorial of 4 is: ",fact(4))
print("factorial of 6 is: ",fact(6))