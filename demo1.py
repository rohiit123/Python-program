stdList=[]
while True:
	print("1. Add Student(no,Name,marks of 3 subjects:)")
	print("2. display all")
	print("3. display result")
	print("4.exit")
	choice=int(input("Enter your choice:"))


	if choice==1:
		rollNo=int(input("Enter rollNo:"))
		name=input("Enter your name:")
		marks1=int(input("Enter your marks1:"))
		marks2=int(input("Enter your marks2:"))
		marks3=int(input("Enter your marks3:"))

		stdRecord={"no":rollNo,"name":Name,"marks":[marks1,marks2,marks3]}
		stdList.append(stdRecord)

	elif choice==2:
		for i in stdList:
			print(i)
	elif choice==3:
	    n=int(input("Enter student rollNo:"))
	    for i in stdList:
	    	if i["no"]==n:
	    	total=sum(i["marks"])
	    	percent=total/3

	    	print(i["no"])
	    	print(i["name"])	
	    	print(i["marks"])
	    	print(total)
	    	print(percent)
	elif choice==4:
		exit()
	else:
		print("Select proper choice")		    		

