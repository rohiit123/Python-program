"""
Given two lists, merge them into a single list 
without modifying the originals.
"""


def merge_lists(list1,list2):
    new_list=[]
    for num in list1:
        new_list.append(num)
    for num in list2:
            new_list.append(num)
    return new_list

nums1=[4,6,7,8]
nums2=[3,6,8,9]
print("The merged list is:",merge_lists(nums1,nums2))