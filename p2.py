marks={"OOAD":90,"DSA":70,"Python":80,"DBS":60,"DAD":40}


for sub,mark in marks.items():
	if mark >=90:
		print("Exllent",sub)
	elif mark >=70 and mark <=70:
		print("Good",sub)
	else:
		print("Need improvement",sub)	

pass_sub=0

for mark in marks.values():
	if mark >=60:
		pass_sub=pass_sub+1		 

print("Student passed in following numbers of subject=",pass_sub)		
