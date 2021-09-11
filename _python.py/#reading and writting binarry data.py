#reading and writting binarry data 

f1=open("guido.png","wb")
f2=open("rossom.jpg","wb")
data=f1.read()
f2.write(data)
print("new image is available with the name")