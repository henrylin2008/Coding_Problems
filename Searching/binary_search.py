# method 1:
# time: O(log(n))
# Space: O(log(n))
# recursive
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        print("no match")
        return -1
    mid = (left+right)//2
    potentialMatch = array[mid]
    if target == potentialMatch:
        print("left, right", left, ",", right)
        print('mid:', mid)
        print("__")
        return mid
    elif target > potentialMatch:  # when target is > potnetialMatch, result is in second half of the array,
                                     moving the mid pointer one position to the right
        print("mid+1:", mid+1)
        print("right:", right)
        print('__')
        return binarySearchHelper(array, target, mid+1, right)
    else:                          # when target is < potnetialMatch, result is in first half of the array,
                                   # moving the mid pointer one position to the left
        print("left:", left)
        print("mid-1:", mid-1)
        print('__')
        return binarySearchHelper(array, target, left, mid-1)

# binarySearch([0,1,21,33,45,55,67,71,78,83], 37)

# ================================================================================
# method 2:
# time: O(log(n))
# space: O(1)
# Iterative
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    while left <= right:
        mid = (left+right) //2
        potentialMatch = array[mid]
        if target == potentialMatch:
            print("match at:", mid)
            return mid
        elif target < potentialMatch:
            right = mid - 1
        else:
            left = mid + 1
    print("no match")
    return -1

# binarySearch([0,1,21,33,45,55,67,71,78,83,88,92], 55)