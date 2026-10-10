a=int(input("enter the number 1:"))
b=int(input("enter the number 2:"))
c=int(input("enter the number 3:"))
if a>b and a>c:
    print(f"{a} is the greater number")
elif b>c and b>a:
    print(f"{b} is the greater number")
else:
    print(f"{c} is the greater number")