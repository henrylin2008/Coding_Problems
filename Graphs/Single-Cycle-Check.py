# link: https://www.algoexpert.io/questions/Single%20Cycle%20Check
# Single Cycle Check
# Difficulty: Medium

# You're given an array of integers where each integer represents a jump of its value in the array. For instance, the
# integer 2 represents a jump of two indices forward in the array; the integer -3 represents a jump of three indices
# backward in the array.
# If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index 0
# brings us to the last index in the array. Similarly, a jump of 1 at the last index in the array brings us to index 0.
# Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single
# cycle occurs if, starting at any index in the array and following the jumps, every element in the array is visited
# exactly once before landing back on the starting index.

# Sample Input:
# array = [2, 3, 1, -4, -4, 2]

# Sample Output:
# true


# Time: O(n)
# Space: O(1)
# Logic: set a variable numElementsVisited to keep track number of elements have visited, and a variable currentIdx to
#        keep track of current index; the goal is while moving around the array, it should return to the first index
#        last. Edge cases to check when there's a loop that it returns to first index before reaching all elements in
#        the array. Run a while loop before less than the length of array, an edge case where if it returns to the first
#        index before reaching all elements in the array, then return False; next increment numElementsVisit by 1, and
#        calculate the next index; use a separate function to find out the next index, which it covers the wrap
#        around cases in the array. For case that is moving forward, next index is calculated as
#        (currentIdx + jump) % len(array); if moving backward, the formula to find out next index:
#        (currentIdx + jump) % len(array) + len(array). Then return true if currentIdx is  at index 0 (starting point)
# conditions:
#       * number of elements visited == len(array)
#       * last Index is back to the initial index (0)
#       * edge case: loop/s that returns to initial index before reaches all elements
#       * next index wrap around cases: moving forward and moving backward
def hasSingleCycle(array):
    numElementsVisited = 0  # number of elements have visited
    currentIdx = 0  # starting index
    while numElementsVisited < len(array):  # when total number of elements visited < len(array)
        if numElementsVisited > 0 and currentIdx == 0:  # in case a repeated loop/s happens before reach all elements
            return False
        numElementsVisited += 1  # increment elements visited
        currentIdx = getNextIdx(currentIdx, array)  # next index
    return currentIdx == 0  # back to the starting index


def getNextIdx(currentIdx, array):
    jump = array[currentIdx]    # how many index have to jump
    nextIdx = (currentIdx + jump) % len(array)  # next index, it covers wrap around cases
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)  # nextIdx + len(array) covers negative case
