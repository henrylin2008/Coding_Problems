# https://www.udemy.com/11-essential-coding-interview-questions/learn/v4/t/lecture/7567172?start=0
# Implement a function that assigns correct numbers in a field of Minesweeper, which is represented as a 2 
# dimensional array 
# Ex: The size of the field is 3x4, and there are bombs at the positions [0,0] (row index=0, column index = 0) and
# [0,1] (row index=0, column index= 1).
# The resulting fields:
# [[-1, -1, 1, 0],
#  [2, 2, 1, 0],
#  [0, 0, 0, 0]]

# Your function should return the resulting 2D array after taking the following three arguments:
# 1. bombs: a list of bomb locations. Given as an array of arrays. Ex: [[0,0],[0,1]]. Assume that three are no
# duplicates
# 2. num_rows: the number of rows in the resulting field.
# 3. num_columns: the number of columns in the resulting field.

# In the resulting fields: 
# * -1 represents that there is a bomb in that location 
# * 1,2,3....etc represents that there are 1,2,3...etc bombs int he surrounding cells 
# * 0 represents that there are no bombs in the surrounds cells

def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row, instead of copying the same list.
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]     # initialize 2D array, num_rows=0, num_cols=0
    print("Init field:", field)
    for bomb in bombs:
        (row_i, col_i) = bomb       # set bomb location, (row index, column index); (bomb[0], bomb[1])
        field[row_i][col_i] = -1    # if the index is a bomb, assign to -1
        # loop through 9 surrounding cells around the bomb cell
        for i in range(row_i - 1, row_i + 2):       # from row_i - 1 to row_i + 1
            for j in range(col_i - 1, col_i + 2):   # from col_i - 1 to col_i + 1
                # if i and j are not out of range and [i][j] != -1
                if 0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1:
                    print("i, j:", i, j)
                    field[i][j] += 1                # increment by 1
                    print("field:", field)
    print("final field: ", field)
    return field


# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
# mine_sweeper([[0, 2], [2, 0]], 3, 3)  # should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)  # should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

# mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)    # should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]
