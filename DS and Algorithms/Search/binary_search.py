# Logic: binary search works on a sorted array; first, define 3 pointers: low, high and mid pointers (in while loop)
# while low pointer <= high pointer, if searching value is > mid pointer, then move low pointer next to mid pointer, and
# update the mid pointer (middle is half of new low pointer and high); elif searching value < mid pointer, move the high
# pointer one position left to the mid pointer, and update the mid pointer (middle in between old low pointer and new
# high pointer). repeat the process until finding the value or return -1 if the searching value is not in the
# input_array.
# Time Complexity: O(log n)
# Best Time: O(1); when the middle index is the value that we are looking for.
# Space Complexity: O(1) (for iterative)
#        O(log n) (for recursive)
def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low + high) // 2     # middle value, int divide
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1   # upper half
        else:
            high = mid - 1  # lower half
    return -1


binary_search([1, 3, 9, 11, 15, 19, 29], 19)
binary_search([1, 3, 9, 11, 15, 19, 29], 20)
