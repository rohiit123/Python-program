# student={"name":"rohit",
# 		"age":21,
# 		"city":"Ahmedabad",
# 		"marks":[79,60,56,90]
# 	}

# for key,val in student.items():
# 	print(key,val)

	# create a dictionary for a student, including
	# keys like name,age,city, and marks(as a list of scores
	# print each piece of information using its key


subjects={"Python":90,
		  "DSA":68,
		  "java":89,
		  "HTML":100,
		  "DBS":90	
		}

key=input("Enter the key:")

if key in subjects:
	print(subjects[key])
else:
	print("Not found")	