# Sum of all the numbers from 1 to 100.

start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))

sum=0

for i in range(start,end+1):
    sum=sum+i
    i+=1

print(sum,end=" ")    