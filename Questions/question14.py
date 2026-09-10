# Sum of all the numbers from 1 to 100 divisible by 2 and 7


start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))

sum=0

for i in range(start,end+1):
    if i % 2 == 0 and i % 7 == 0:
        print(i)
        sum=sum+i
    i+=1
    
print(f"sum of all the numbers which are divisible by 2 and 7 are={sum} ")        
