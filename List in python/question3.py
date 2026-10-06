"""
Reverse a list without using the .reverse() method
or list slicing ([::-1]).

"""

def reverse_list(lst):
    new_list=[]
    n=len(lst)
    for i in range(n-1,-1,-1):
        new_list.append(lst[i])
    return new_list

nums=[3,5,6,7,200,89,100,40,90]
reversed_nums=reverse_list(nums)
print("Original list:", nums)
print("Reversed list:", reversed_nums)
        