# method 1:
# time: O(log(n))
# Space: O(log(n))
# recursive
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2  # middle pointer index, rounded down with //2
    potentialMatch = array[mid]  # value at middle pointer
    if target == potentialMatch:
        return mid  # index of mid pointer
    elif target > potentialMatch:  # eliminate first half from the array, and set left pointer = mid (pointer) + 1
        return binarySearchHelper(array, target, mid + 1, right)
    else:  # eliminate second half from the array, and set the right pointer = mid (pointer) - 1
        return binarySearchHelper(array, target, left, mid - 1)


# binarySearch([0,1,21,33,45,55,67,71,78,83], 37)

# ================================================================================
# method 2:
# time: O(log(n))
# space: O(1)
# Iterative
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        potentialMatch = array[mid]
        if target == potentialMatch:
            # print("match at:", mid)
            return mid
        elif target < potentialMatch:
            right = mid - 1
        else:
            left = mid + 1
    # print("no match")
    return -1

# binarySearch([0,1,21,33,45,55,67,71,78,83,88,92], 55)
