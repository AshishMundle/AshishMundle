# wap to check wheather a number is divisible by 5 and 11 or not


a=float(input("enter a number : "))

if a%5==0:
    print("it is divisible by 5")
elif a%11==0:
    print("it is divisible by 11")
else :
    print("not divisible by 5 and 11")