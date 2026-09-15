"""
* 
* *
* * *
* * * *
* * * * *

"""

row=int(input("Enter the numbers of rows you want:"))
column=int(input("Enter the number of columns you want:"))

for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")

    print()    