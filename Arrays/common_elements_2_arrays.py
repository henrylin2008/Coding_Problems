# 11 essential Coding questions
# Write a function that returns the common elements (as an array) between 
# 2 sorted arrays of integers (ascending order)
# Ex: the common elements between [1,3,4,6,7,9] and [1,2,4,5,9,10] are [1,4,9]
# Note: we're going to use lists instead of arrays in Python for simplicity

def common_elements(list1, list2):
    p1 = 0
    p2 = 0
    # an empty list
    result = []
    while p1 < len(list1) and p2 < len(list2):
        # if first item in list1 and list2 are the same
        # then add the item to the (result) list, and increment p1 and p2
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
        # if p1 in list1 is > p2 in list 2, then increment p2 by 1 (or to next item in list2)
        elif list1[p1] > list2[p2]:
            p2 += 1
        # if opposite, then increment p1 by 1 (or the next item in list1)
        else:
            p1 += 1
    # return result list
    return result


# NOTE: The following input values will be used for testing your solution.
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
# common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# common_elements(list_b1, list_b2) should return [] (an empty list).