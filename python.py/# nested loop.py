# nested loop 

# -----------------------------------

for i in range (1,5):
    for j in range (1,5):
        print (i,end=' ')
    print () 


#------------------------------------

for i in range (1,5):
    for j in range (1,5):
        print (i,end='')
    print ()


#------------------------------------

for i in range (1,5):
    for j in range (1,i+1):
        print (i,end='')
    print ()


#------------------------------------

for i in range (1,5):
    for j in range (1,i+1):
        print ('*',end='')
    print ()


#-------------------------------------

x=1
for i in range (1,5):
    for j in range (1,5):
        print(x,' ',end=' ')
        x=x+4
    print ()
    