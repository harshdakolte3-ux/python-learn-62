units = int(input("enter the units"))
if (units <=100):
    print(units*1)
elif (units >=100 and units <=200):
    diff = units-100
    bill = units+diff*2
    print(bill)
elif (units <200):
    diff = units -200
    bill = units+diff*3
    print(bill)
else:
    print("negative number")
