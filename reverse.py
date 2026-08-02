num=int(input("Enter a number to reverse:"))
while num>0:
    last_digit=num%10
    print(last_digit)

    num=num//10