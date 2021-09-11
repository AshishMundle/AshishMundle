#wap to input month number and print no of days in that months

month_name = input("enter month name :")
if month_name =="february":
    print("no of days : 28/29 days")
elif month_name in ("april","june","september","november"):
    print("no of days : 30 days")
else :
    print(" no of days : 31 days")