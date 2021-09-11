# function 

#--------------------------------------

def wish ():
    print ("hello good morning")
wish()
wish()
wish()


#---------------------------------------

def wish (name): 
    print ("hello",name,"good morning")
wish("ashish")
wish("amar")
wish("gaurav")


#---------------------------------------

def findsquare (n):
    print("square of ",n,"is",n*n)
findsquare(5)


#----------------------------------------

def add (x,y):
    return x+y
res=add(10,20)
print('the sum is ',res)
print('the sum is ',add (55,22))


#----------------------------------------

#check no is even or add 

def oddeven (n):
    if n%2==0:
        print(n,'is even number')
    else :
        print(n,'is odd number')
oddeven(8)
oddeven(5)