# Ask a number from the user and print all the factors

num=int(input("Enter the number:"))
count=0
i=1
while i<=num:
    if num % i==0:
        count=count+i
        print(i,end=" ")
    i+=1   
print(f"Total of all the factors{count}")     