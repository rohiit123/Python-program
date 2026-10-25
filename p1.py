# nums=[]
# length=int(input("Enter the length of list:"))
# for i in range(length):
# 	n=int(input("Enter the integers for your list:"))
# 	nums.append(n)

# even=[]
# odd=[]
# for n in nums:
# 	if n % 2==0:

# 		even.append(n)		
# 	else:	
# 		odd.append(n)
# print("The original list:",nums)
# print("Even list:",even)	
# print("Odd list:",odd)


# nums=[]
# leng=int(input("Enter the length: "))

# for i in range(leng):
# 	lis=int(input("Enter the value:"))
# 	nums.append(lis)


# print("List of nums is:",nums)

# heighest=nums[0]
# second=nums[0]

# for n in nums:
# 	if n > heighest:
# 		second=heighest
# 		heighest=n	
# 	elif n > second and n< heighest:
# 		second = n 

# print("The heighest value:",heighest)
# print("The second heighest value:",second)	



# names=[
# 	"Raj", 
# 	"Rohit",
# 	"Moon",
# 	"dhruv",
# 	"Moon",
# 	"Moon",
# 	"Rohit"
# ]	


# for name in names:
# 	count=0
# 	for n in names:
# 		if name==n:
# 			count=count+1
# 	print(name,count  )		
# 		



# lst=[]
# length=int(input("Enter the length:"))
# for i in range(length):
# 	n=int(input("Enter the values:"))
# 	lst.append(n)

# even=0
# odd=0

# for n in lst:
# 	if n % 2 == 0:
# 		even = even+1
#     else:
#     	odd = odd+1
    	

# print("Odd numbers:",odd)
# print("Even numbers",even)    			 



# lst = []
# length = int(input("Enter the length: "))

# for i in range(length):
#     n = int(input("Enter the values: "))
#     lst.append(n)
# print(lst)
# even = 0
# odd = 0

# for n in lst:
#     if n % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1

# print("Odd numbers:", odd)
# print("Even numbers:", even)



student_marks={"hindi":77,
   			   "english":67,
   			   "science":90,
   			   "python":90,
   			   "dsa":50	  
              }

marks="python"

ans=student_marks.get(marks)
 
if ans is None:
	print("Key not found")
else:
	print(ans)	





