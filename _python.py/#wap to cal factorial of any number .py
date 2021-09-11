#wap to cal factorial of any number 

num=int(input("enter the number: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("factorial is ",factorial)