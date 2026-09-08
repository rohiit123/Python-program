start=int(input("Enter the start value:"))
end=int(input("Enter the end value:"))



i=start
total=0
while i<=end:
    if i % 2 ==0 and i % 7 ==0:
        print(i,end=" ")
        total=total+i
    i+=1

print(f"Total of all the number which are divisible by 2 and 7:{total}")        