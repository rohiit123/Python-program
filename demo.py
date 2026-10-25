name=input("Enter your name:")
age=int(input("Enter your age:"))
city=input("Enter your city:")
no_email=int(input("How many email do you have?:"))
email_list=[]

for i in range(1,no_email+1):
	email=input("Enter your email:")
	email_list.append(email)


dict1={"name":name,"age":age,"city":city,"email":email_list}

print(dict1)
