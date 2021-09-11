# global keyword 

a=20

def fun1 ():
    global a
    a=55
    print(a)
     
def fun2 ():
    print(a)

def fun3 ():
    print(a)

fun1 ()
fun2 ()
fun3 ()