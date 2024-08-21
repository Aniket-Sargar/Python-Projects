#Tax Calculator based on Salary/Income

Income = int(input("Enter Your Annula Income: "))

if(Income < 250000):
    print("Tax = ",Income * 0.0)#0% tax
elif(Income >= 250000 and Income < 500000):
    print("Tax = ",Income * 0.05)#5% tax
elif(Income >= 500000 and Income < 750000):
    print("Tax = ",Income * 0.10)#10% tax
elif(Income >= 750000 and Income < 1000000):
    print("Tax = ",Income * 0.15)#15% tax
elif(Income >= 1000000 and Income < 1250000):
    print("Tax = ",Income * 0.20)#20% tax
elif(Income >= 1250000 and Income < 1500000):
    print("Tax = ",Income * 0.25)#25% tax
else:
    print("Tax = ",Income * 0.30)#30% tax for above 15 lakh


# Note:

#     --> This tax slab is based on Indian Tax system.
#     --> Based on financial year 2023-2024.

