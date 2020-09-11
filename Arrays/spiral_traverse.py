# https://www.algoexpert.io/questions/Spiral%20Traverse
# Difficulty: Medium
# Spiral Traverse
# Write a function that takes in an n x m two-dimensional array (that can be square-shaped
# when n == m) and returns a one-dimensional array of all the array's elements in spiral order.
# spiral order starts at the top left corner of the two-dimensional array, goes to the right,
# and proceeds in a spiral pattern all the way until every element has been visited.
#
# Sample Input:
# array = [
#   [1,   2,  3, 4],
#   [12, 13, 14, 5],
#   [11, 16, 15, 6],
#   [10,  9,  8, 7],
# ]

# Sample Output:
# [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# Solution #1
# O(n) time | O(n) space - where n is the total number of elements in the array
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            # Handle the edge case when there's a single row in the middle
            # of the matrix. In this case, we don't want to double-count the values
            # in this row, which we've already counted in the first for loop above.
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            # Handle the edge case when there's a single column in the middle
            # of the matrix. In this case, we don't want to double-count the values
            # in this column, which we've already counted in the second for loop above.
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result