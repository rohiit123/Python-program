# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3 
# 2 2 2 2 2 
# 1 1 1 1 1 

row=int(input("Enter the numbers of rows you want:"))
column=int(input("Enter the number of columns you want:"))

for i in range(row,0,-1):
    for j in range(1,column+1,):
        print(i,end=" ")
    
    print()  