"""
1 
2 1 
3 2 1 
4 3 2 1
5 4 3 2 1 
"""
row=int(input("Enter the numbers of rows you want:"))
column=int(input("Enter the number of columns you want:"))

for i in range(1,row+1):
    for j in range(i,0,-1):
        print(j,end=" ")

    print()    