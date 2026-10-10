unit=int(input("enter the number of the units consumed:"))
if unit<=100:
    bill=unit*1.5
elif unit<=200:
    bill=100*1.5+(unit-100)*2.5
else:
    bill=100*1.5+100*2.5+(unit-200)*4
print("the total electricity bill is ",bill)