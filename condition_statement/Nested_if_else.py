age=int(input("Enter your age:"))
certificate=True


if age>=18:
    if certificate==True:
        print("You are hired for the job")
    else:
        print("Sorry,You need certificate for the job")    
else:
    print("Can not hire, your age is less than 18")


   



