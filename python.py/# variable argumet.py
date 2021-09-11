# variable argumet 

def sum (*n):
    total1=0
    for i in n:
        total1=total1  + i
    print("sum= ", total1)

sum()
sum(10,20)
sum(10,20,30,40)
