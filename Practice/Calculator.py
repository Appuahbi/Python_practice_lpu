first =int(input("Enter the first number : "))
operater=input("Enter operater (+,-,*,/,%) : ")
second=int(input(" Enter second number : "))
if operater=="+":
    print(first+second)
elif operater=="-":
    print(first-second)
elif operater=="*":
    print(first*second)
elif operater=="/":
    print(first/second)
elif operater=="%":
    print(first%second)
else:
    print("Invalid operater")