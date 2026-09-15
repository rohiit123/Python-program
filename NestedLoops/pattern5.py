"""
1 
1 2 
1 2 3 
1 2 3 4
1 2 3 4 5 
"""
row=int(input("Enter the numbers of rows you want:"))
column=int(input("Enter the number of columns you want:"))

for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")

    print()    