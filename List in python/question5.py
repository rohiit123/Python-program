"""
Given a list, remove all duplicate elements while
preserving the original order of the unique items.

"""



def remove_duplicates(lst):
    new_list=[]
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list


nums=[3,3,3,3,3,5,5,5,7,8,9,10,20,]
print("The list after removing duplicates is:", remove_duplicates(nums))