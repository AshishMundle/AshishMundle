# print all even and odd numbers from 1 to 50 

even=0
odd=0
for x in range (1,50):
    if x%2==0:
        even=even+1
    else:
        odd=odd+1
print("total even no are ",even,"odd no are ",odd)