"""
Write a program that takes a list of numbers and,
using a loop, determines whether the list is sorted in 
asscending order.Print True if it is sorted, and False otherwise.
"""


def is_sorted(lst):
    n=len(lst)
    for i in range(0,n-1):
        if lst[i]>lst[i+1]:
            return False
    return True

nums=[3,5,6,7,500,89,100,280]
nums1=[3,7,8,9,10,40,50,90,100]
print("Is the list sorted in ascending order?",is_sorted(nums))    
print("Is the list sorted in ascending order?",is_sorted(nums1))    