"""
Given a list of numbers, write python code using
a loop to find and print the largest element.Do not
use the built-in max() function.
"""


nums=[0,5,12,45,17,98,100,45,1000]

maxi=float("-inf")

for num in nums:
    if num > maxi:
        maxi=num


print(f"Maximum number = {maxi}")


