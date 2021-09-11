# write a program to calculate profit or loss

a=float(input("enter cost price :"))
b=float(input("enter selling price : "))
P= b-a
L= a-b
if P>L:
    print("profit")
    print("the profit is :",P)
else:
    print("loss")
    print("the loss is ",L)