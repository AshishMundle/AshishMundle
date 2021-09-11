#file handling example

f=open("myfile.txt","w")
print("name of file",f.name)
print("file mode",f.mode)
print("readable",f.readable())
print("writable",f.writable())
print("file has closed",f.closed)
f.close()
print("file has closed",f.closed)