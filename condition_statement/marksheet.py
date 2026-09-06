marks=int(input("Enter your marks:"))

if marks>=90 and marks <=100:
    print("Grade is A")
elif marks>=80 and marks<90:
    print("Gread is B")
elif marks>=70 and marks<80:
    print("Gread is C")
elif marks>=60 and marks<70:
    print("Gread is D")
elif marks>=0 and marks <=60:
    print("You have failed the exam!")   
else:
    print("Invalid input!!!!!!!")            