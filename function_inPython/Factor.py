"""
Write a function that prints all the factors of a number entered by user
"""


def factor_num():
    num=int(input("Enter your number:"))
    for i in range(1,num+1):
        if num % i ==0:
            print("The factor are :",i)
        i+=1    


factor_num()
factor_num()