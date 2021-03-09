# Rotating a 2D array by 90 degrees
# A 2-dimensional array is an array of arrays
# Implement a function that takes a square 2D array (# columns = # rows) and rotates it by 90 degrees

# Ex:
# [[1, 2, 3],                   [[7, 4, 1],
#  [4, 5, 6],       -->          [8, 5, 2],
#  [7, 8, 9]]                    [9, 6, 3]]

# Solve this problem in place, means that your function won't create a new array to solve this problem. Instead, modify
# the content of the given array with O(1) extra space.

# Out-of-space solution: create another copy of array
import copy


# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    rotated = copy.deepcopy(given_array)     # new array, copy of the original array
    for i in range(n):                       # i: row index
        for j in range(n):                   # j: column index
            (new_i, new_j) = rotate_sub(i, j, n)        # find new coordinates by using rotate_sub function
            rotated[new_i][new_j] = given_array[i][j]   # new position
    print("Rotated:", rotated)
    return rotated


# return new coordinates of the rotated position
def rotate_sub(i, j, n):    # i: original row index, j: original column index; n = number of rows/columns
    return j, n - 1 - i     # new_i = j (new row index), new_j = n-1-i (new column index)


a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
rotate(a1, 3)   # should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
rotate(a2, 4)  # should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]