"""
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
"""
row=int(input("Enter the numbers of rows you want:"))
column=int(input("Enter the number of columns you want:"))

for i in range(row,0,-1):
    for j in range(i,0,):
        print(i,end=" ")

    print()    