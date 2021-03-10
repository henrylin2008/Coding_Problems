# Rotating a 2D array by 90 degrees
# A 2-dimensional array is an array of arrays
# Implement a function that takes a square 2D array (# columns = # rows) and rotates it by 90 degrees

# Ex:
# [[1, 2, 3],                   [[7, 4, 1],
#  [4, 5, 6],       -->          [8, 5, 2],
#  [7, 8, 9]]                    [9, 6, 3]]

# Solve this problem in place, means that your function won't create a new array to solve this problem. Instead, modify
# the content of the given array with O(1) extra space.

# In-place solution:
# return new coordinates of the rotated position without creating a new array
import math


# find and return the new position's coordinates: (new_i, new_j)
def rotate_sub(i, j, n):    # i: original row index, j: original column index; n = number of rows/columns
    return j, n - 1 - i     # new_i = j (new row index), new_j = n-1-i (new column index)


# Space: O(1); in-place: using existing array
# main function, create a tmp array, and utilize the rotate_sub function to set each value in tmp array, then use the
# values in tmp array to set given_array's values (ex: tmp[3] = given_array[0], tmp[0] = given_array[1])
def rotate(given_array, n):                     # n: number of rows/columns
    for i in range(math.ceil(n/2)):             # columns; math.ceil covers odd and even rows
        for j in range(math.floor(n/2)):        # rows
            tmp = [-1] * 4                      # initialize temp array of 4 values that to be shuffle around
            (current_i, current_j) = (i, j)     # current_i, current_j points to the item is currently examing
            for k in range(4):      # This loop sets new values (from given_array) for the temp array
                tmp[k] = given_array[current_i][current_j]  # store current (i, j) to temp array's current position
                (current_i, current_j) = rotate_sub(current_i, current_j, n)    # get next position
            for v in range(4):      # this loop uses values from the temp array to rotate & set given_array's values
                # current position of given array = previous position of temp array; tmp[(0-1)%4] = tmp[3] (last value)
                given_array[current_i][current_j] = tmp[(v - 1) % 4]  # tmp[(k-1)%4]: temp array's previous position
                (current_i, current_j) = rotate_sub(current_i, current_j, n)    # next position
    # print("array:", given_array)
    return given_array

# # Out-of-Place solution: create another copy of array
# import copy
#
#
# # n = # rows = # columns in the given 2d array
# def rotate(given_array, n):
#     rotated = copy.deepcopy(given_array)     # new array, copy of the original array
#     for i in range(n):                       # i: row index
#         for j in range(n):                   # j: column index
#             (new_i, new_j) = rotate_sub(i, j, n)        # find new coordinates by using rotate_sub function
#             rotated[new_i][new_j] = given_array[i][j]   # new position
#     print("Rotated:", rotated)
#     return rotated
#
#
# # return new coordinates of the rotated position
# def rotate_sub(i, j, n):    # i: original row index, j: original column index; n = number of rows/columns
#     return j, n - 1 - i     # new_i = j (new row index), new_j = n-1-i (new column index)


#
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
# rotate(a1, 3)   # should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
# rotate(a2, 4)  # should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]