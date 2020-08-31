# 11 essential Coding questions
# Find the most frequently occurring item in an array. 
# Ex: the most frequently occurring item in [1,3,1,3,2,1] is 1.
# if you're given an empty array, you should return None
# Note: we're going to use lists instead of arrays in Python for simplicity 


def most_frequent(given_list):
    max_count = -1  # keep track of max_item has appeared
    max_item = None  # most frequent occurred seem so far
    count = {}  # empty hash table or dictionary (to keep track of number of time each item has appeared)
    for i in given_list:
        if i not in count:  # if current value is not in the count dictionary, initialize item and count: item 1,
            count[i] = 1    # count so far: 1
        else:
            count[i] += 1   # else increase the count by 1
        if count[i] > max_count:    # if current count > max_count
            max_count = count[i]    # max_count = current values
            max_item = i    # update most frequent item
    return max_item


# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1.
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3.
list2 = [3, 3, 1, 3, 2, 1]
# # most_frequent(list3) should return None.
list3 = []
# # most_frequent(list4) should return 0.
list4 = [0]
# # most_frequent(list5) should return -1.
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

most_frequent(list2)

