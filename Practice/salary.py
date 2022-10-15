a=int(input("Time spent in the company:"))
salary=int(input("Enter the salary:"))
if a>10:
    print("the net bonus =",salary+salary*0.1)
elif a>6 and a<10:
    print("the net bonus =",salary+salary*0.08)
elif a<6:
    print("the net bonus =",salary+salary*.05)
else:
    print("no salary")
