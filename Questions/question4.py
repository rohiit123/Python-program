# Take a person's age and whether they have a valid ID (True/false) as input.
# They can enter a venue only if they are 18 or AND have valid ID. Printthe appropriate message


age=int(input("Enter the age:"))
id=input("Do you have your ID(True/False):")


if age >= 18:
    if id=="True":
        print("You can enter in a venue")
    else:
        print("You need your valid id")    
else:
    print("Your age is less than 18")