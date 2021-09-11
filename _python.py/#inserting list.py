#inserting list 

f=open("covid.txt","w")
mylist=["prashant ","mahesh ","suresh "]      # we can only pass string not float or int 
f.writelines(mylist)
print("written work completed")
f.close()