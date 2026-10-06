"""
Given two list of the same length,write a python code
using a loop to create a new list where each element is the sum
of the corresponding elements from both original lists.


"""
def sum_of_two_lists(list1, list2):
    new_list=[]
    n=len(list1)
    for i in range(0,n):
        total=list1[i]+ list2[i]
        new_list.append(total)
    return new_list

nums1=[4,5,2,9,5,8,0,-20,40]
nums2=[7,8,-2,4,5,7,50,20,10]
result=sum_of_two_lists(nums1,nums2)
print("The sum of the two lists is:",result)    