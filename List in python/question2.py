"""
Write a program that takes a list and a target number.
Use a loop to determine if the target number exists in
the list.Do not use the in operator
"""

def does_target_exists(lst,target):
    for num in lst:
        if num == target:
            return True
    return False


nums=[5,12,68,93,45,40,42,30]

print(does_target_exists(nums,12))