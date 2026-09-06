# A shop gives discount based on purchase amount:
# Above 5000--> 20% discount
# Above 2000--> 10% discount
# Above 1000--> 5% discount
# 1000 or below--> no discount


Amount=int(input("Enter the purchased amount:"))

if Amount>= 5000:
    print("You got discount of 20%")
elif Amount >2000 and Amount <5000:
    print("You got discount of 10%")
elif Amount >1000 and Amount < 2000:
    print("You got discount of 5%")
elif Amount<1000 or Amount <0:
    print("No discount")

            