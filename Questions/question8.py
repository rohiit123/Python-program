# Sum of all the number from 1 to 100

end=int(input("Enter the end value:"))

i=1
sum=0
while i<=end:
    sum=sum+i
    i+=1

print(f"Total of all the number are {sum}")