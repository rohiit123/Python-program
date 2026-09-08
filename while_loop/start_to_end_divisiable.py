# Print start to end divisiable by 4 and 3 


start=int(input("Enter the start value:"))
end=int(input("Enter the end value:"))

i=start

while i<=end:
    if i%3==0 and i%4==0:
        print(i,end=" ")
    i+=1    