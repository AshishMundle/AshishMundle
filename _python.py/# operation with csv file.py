# operation with csv file

import csv
f=open("student.csv","w",newline="")
a=csv.writer(f)               #here it will return csvwriter object
a.writerow(["rollno","name","mobileno"])

rollno=1001
name="prashant"
mobileno=6464646464

#rollno=int(input("enter roll no :- "))
#name=input("enter your name :- ")
#enter mobileno=int(input("enter mobile number :- "))

a.writerow([rollno,name,mobileno])
print("record are save")