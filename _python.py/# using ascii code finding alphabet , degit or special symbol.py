# using ascii code finding alphabet , degit or special symbol

ch=input("enter character : ")
if (ord(ch)>=48 and ord(ch)<=57):
    print("the given character is a digit")
elif((ord(ch)>=65 and ord(ch)<=90)or (ord(ch)>=97 and ord(ch)<=122)):
    print("the given character is alphabet")
else:
    print("the given character is special symbol")