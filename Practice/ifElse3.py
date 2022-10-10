#mark list
mark=int(input("Enter your marks : "))
if mark > 70 and mark<=80:
    print("Your grade is A")
elif mark > 60 and mark<=70:
    print("Your grade is B")
elif mark > 50 and mark<=60:
    print("Your grade is C")
else:
    print("Sorry not eligible for higher studies")