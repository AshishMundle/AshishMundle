# using seek function 

f=open("myfile.txt","r")
print("total data_",f.read())
print("current position of cursor",f.tell())
f.seek(5)
print("the currentposition of cursor",f.tell())
print(f.read())
f.close()