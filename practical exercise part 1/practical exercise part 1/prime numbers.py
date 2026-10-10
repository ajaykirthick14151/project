n=int(input("enter the number"))
isprime=True
if n<=1:
    isprime=False
else:
    for i in range(2,n):
        if n%1==0:
            isprime=False
            break
if isprime:
    print("the number is prime")
else:
    print("the number is not prime")