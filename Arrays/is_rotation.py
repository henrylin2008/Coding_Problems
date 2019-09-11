# 11 essential Coding questions
# Write a function that returns True if one array is a notation of another
# ex: [1,2,3,4,5,6,7] is a notation of [4,5,6,7,1,2,3].
# Note: there are no duplicates in each of these arrays
# Reminder: We're going to use lists instead of arrays in Python for simplity

def is_rotation(list1, list2):
    # if list1.length != list2.length: return False
    if len(list1) != len(list2):
        return False
    # First element in list1 (assumption)
    key = list1[0]
    # key index in list2
    key_loc = -1

    #for i from 0 to list2.length - 1:
    #   if list2[i] == key:
    #       key_i = i
    #       break
    for i in range(len(list2)):
        if list2[i] == key:
            key_loc = i
            break

    # if key_i == -1: return False
    if key_loc == -1:
        return False

    # for i from 0 to list1.length - 1:
    #   j = (key_i + i)%list1.length
    #   if list1[i] != list2[j]: return False
    for i in range(len(list1)):
        j = (key_loc + i) % len(list1)
        if list1[i] != list2[j]:
            return False
    return True

# Run Time: O(n)


# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
