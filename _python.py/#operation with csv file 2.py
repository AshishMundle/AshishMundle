 #operation with csv file 2

import csv
f=open("student.csv","w", newline="")
a=csv.writer(f)
a.writerow(["name","rollno","email","address","mobileno","p1","p2","p3","p4","p5","total","percentage","result"])

name="ashish"
rollno=1119
email="xyz@gmail.com"
address="nagpur"
mobileno=8989898989
p1=80
p2=78
p3=98
p4=95
p5=90
total=p1+p2+p3+p4+p5
percentage= total/5

if p1>35 and p2>35 and p3>35 and p4>35 and p5>35 :
        result = "pass"
        print("pass")
else:
        pass
        result = "fail"

a.writerow([name,rollno,email,address,mobileno,p1,p2,p3,p4,p5,total,percentage,result])
print("record are save")