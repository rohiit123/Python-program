dicts={"a":20,
	   "b":30,
	   "c":40,
	   "d":50,
	   "e":50,
	   "f":20,
	   "g":20
      }

for key in dicts:
	count=0

	for value in dicts.values():
		if dicts[key]==value:
			count=count+1
	print(key," ",dicts[key]," ",count)			
 




key = input("Enter a key:")
if key in dicts:
	print("key found",key)
else:
	print("Key not found",key)	


total=0

for value in dicts.values():
	total=total+value
print("Total sum is:",total)		      

highest=0

for value in dicts.values():
	if value > highest:
		highest = value

print("highest value is:",highest)		



