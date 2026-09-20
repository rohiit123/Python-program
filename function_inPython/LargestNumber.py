"""
Write a function called find_max that takes three numbers as 
parameters and prints the largest one
"""

def find_max(a,b,c):
    if a>b and a>c:
        print("A is largest which is=",a)
    elif a<b and b>c:
        print("B is largest which is=",b)
    else:
        print("C is largest which is=",c)


find_max(20,50,12)  
find_max(22,-10,100)              
find_max(-1,-10,-30)