start=int(input("Enter the start value:"))
end=int(input("Enter the end value:"))

i=start

while i<=end:
    if i % 2 == 0:
        print(i, end=" ")
    i+=1