# wap to check it is alphabet ,digit or special character

x=input("enter the character :")

if ((x>="a" and x<="z")or(x>="A" and x<="Z")):
    print("character is alphabet")
elif (x>='0' and x<='9'):
    print("character is numeric")
else :
    print(" character is special sxmbol")
    