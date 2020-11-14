# ZigZag Traverse
# Difficulty: Hard
# link: https://www.algoexpert.io/questions/Zigzag%20Traverse

# Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a
# one-dimensional array of all the array's elements in zigzag order.
# Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element, and proceeds in a
# zigzag pattern all the way to the bottom right corner.

# Sample Input:
# array = [
#   [1,  3,  4, 10],
#   [2,  5,  9, 11],
#   [6,  8, 12, 15],
#   [7, 13, 14, 16],
# ]

# Sample Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Time: O(n), where n is the total number of elements in the two-dimensional array
# Space: O(n), where n is the total number of elements in the two-dimensional array
# Solution: set boundaries:
# If the direction is going down; boundaries: first column and last row; If it's the first column, move direction
# straight down; elif it's last row, move straight right by 1; else move down 1 row and 1 to the left;
# If the direction is going up, boundaries: first row and last column; if is the final column, moving straight down 1;
# elif is the first row, move to the right by 1; else: move one row up and one column right
# append everything in the passing path into the result array

def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1   # length of first subarray - 1
    result = []     # append the values into this array
    row, col = 0, 0     # current/starting position
    goingDown = True    # goingDown direction
    while not isOutOfBounds(row, col, height, width):   # while is not out of bounds
        result.append(array[row][col])  # append current value to the result array (since it's inbound)
        if goingDown:   # if going down
            if col == 0 or row == height:   # if first column or last row
                goingDown = False   # changing direction (going up), as it hits the left/bottom boundaries
                if row == height:   # if at the bottom row of the array
                    col += 1    # moves to the right by 1
                else:   # else if at the first column (but not last row)
                    row += 1    # going directly down by 1
            else:   # not first column or last row, but going diagonal down
                row += 1    # down 1
                col -= 1    # left 1
        else:   # else if going up
            if row == 0 or col == width:    # if top row or last column, the boundaries
                goingDown = True    # going down, since else (outer loop) is going up,
                if col == width:    # if in the final column
                    row += 1    # going directly down by 1
                else:   # first row but not on the top right corner
                    col += 1    # move to right by 1
            else:   # in middle of the array, going (diagonal) up
                row -= 1    # going up by 1
                col += 1    # going right by 1
    return result


def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width
    # row < 0: too high up, or row before the first row
    # row > height: too low, or out of bound from the bottom row
    # col < 0: too far from the left, or col left to the first column
    # col > width: too far from the right, or column after the last column
