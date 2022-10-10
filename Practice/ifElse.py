#Take x and y two variables and assign them value
#if x is less than y,print YAYY
#else print NAYY
x=23
y=56
if x>y:
    print("YAYY")
else:
    print("NAYY")






#take values of length and breadth from user
#print if it is a square or not
Length=int(input("Enter the length : "))
Breadth=int(input("Enter the breadth : "))
if Length==Breadth:
    print("It is a square")

else:
    print("it is not a square")









#A Company decided to give bonus of 1000Rs to
#employe if his/her service is more than 5 years
#Ask user their salary and year of service and print
#the net bonus amount

c=int(input("salary : "))
d=int(input("How many years of service : "))
e=1000
if d > 5:
    print("Eligible for 1000Rs bonus")
    print(c+e)
else:
    print("Not eligible for bonus")





