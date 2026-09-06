# Take three numbers as input.Print the largest of the three without using any
# built-in function


num1=int(input("Enter the value of number 1:"))
num2=int(input("Enter the value of number 2:"))
num3=int(input("Enter the value of number 3:"))

if num1 > num2 and num1 >num3:
    print("Number 1 is grater")
elif num1 < num2 and num2 > num3:
    print("Number 2 nis grater")
else:
    print("Number 3 is greater")        