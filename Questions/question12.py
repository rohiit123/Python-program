# Print all the number which are divisible by 3 and 5
# from 1 to 100.

start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))


for i in range(start,end+1):
    if i%3==0 and i%5==0:
        print(i,end=" ")
    i+=1    