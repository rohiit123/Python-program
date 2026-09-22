"""
Write a function tax_calculator(income) that takes 
annual income and returns the tax amount based on these slabs:
-->Up to 250000  --> No tax
-->250000 to 500000-->5%
-->500000 to 1000000-->20%
-->above 1000000-->30%

"""


def tax_calculator():
    income=int(input("Enter your income:"))
    if income<=250000:
        return "No tax"
    elif income>=250001 and income<=500000:
        return (income*5)/100
    elif income>=500001 and income<=1000000:
        return (income*20)/100
    return (income*30)/100


print(tax_calculator())