#program without using and using lambda  function 


#without using lambda function 

def even(x):
    if x%2==0 :
        return True  
    else:
        return False
lis=[0,5,10,15,20,25,30]
l1=list(filter(even,lis))
print(l1)


#using lambda function

l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,1))
print (l1)
l2=list(filter(lambda x:x%2!=0,1))
print (l2)