
#A Company decided to give bonus of 1000Rs to
#employe if his/her service is more than 5 years
#Ask user their salary and year of service and print
#the net bonus amount

c=int(input("salary : "))
d=int(input("How many years of service : "))
e=1000
if d > 5:
    print("Eligible for 1000Rs bonus")
    print("Net bonus amount is :",c+e)
else:
    print("Not eligible for bonus")