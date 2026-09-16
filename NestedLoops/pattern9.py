"""
5 4 3 2 1 
4 3 2 1 
3 2 1
2 1
1
"""
row=int(input("Enter the numbers of rows you want:"))

for i in range(row,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")

    print()    